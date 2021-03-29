# -*- coding: utf-8 -*-
import scrapy
import w3lib.html
import datetime
import json

class SANewsSpider(scrapy.Spider):
    name = "sa-news"
    start_urls = [
        'https://seekingalpha.com/market-news',
    ]
    headers= {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        for quote in response.css("#all-news ul.item-list li.item h4 a"):
            yield scrapy.Request(
                'https://seekingalpha.com/api/v3/news/' + self.article_id_from_href(quote.attrib['href']) + '?include=author%2CprimaryTickers%2CsecondaryTickers%2CreadNowSuggestion%2CotherTags',
                self.parse_article,
                headers=self.headers
            )
                                            
    def article_id_from_href(self, href):
        return href.split('-')[0].split('/')[-1]

    def parse_article(self, response):
        jsonres = json.loads(response.text)
        data = jsonres['data']
        included = jsonres['included']
        url = 'https://seekingalpha.com' + data['links']['self']
        author_id = data['relationships']['author']['data']['id']
        author_name = ''
        for inc in included:
            if author_id == inc['id']:
                author_name = inc['attributes']['nick']
        yield {
            'originalUrl': url,
            'url': url,
            'title': data['attributes']['title'],
            'content': w3lib.html.remove_tags(data['attributes']['content']).strip(),
            'author': {'name': author_name},
            'publishedDate': data['attributes']['publishOn'],
            'estimatedPublishedDate': data['attributes']['publishOn'],
            'harvestDate': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            # 'stockTicker': ticker_symbol,
            'index-date': data['attributes']['publishOn'],
            'duplicateGroupId': 'S' + str(hash(url)), #signify it came from scrapy and not lexis
            'languageCode': 'en'
        }
