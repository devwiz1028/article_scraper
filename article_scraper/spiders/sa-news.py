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

    def parse(self, response):
        for quote in response.css("#all-news ul.item-list li.item h4 a"):
            yield scrapy.Request('https://seekingalpha.com' + quote.attrib['href'], self.parse_article)

    def parse_article(self, response):
        script_json = response.css('script[type="application/ld+json"]::text').extract_first()
        script_dict = json.loads(script_json)
        try:
            ticker_symbol = script_dict['about'][0]['tickerSymbol']
        except:
            ticker_symbol = ''
        yield {
            'originalUrl' : response.url,
            'url' : response.url, #to match lexis format
            'title': response.css("#mc-hd h1::text").extract_first(),
            'content': w3lib.html.remove_tags(response.css("#mc-body #bullets_ul").get()).strip(),
            'author': {'name': response.css(".mc-info a[rel=author] span::text").extract_first()},
            'publishedDate': response.css(".mc-info time::text").extract_first(),
            'estimatedPublishedDate': response.css(".mc-info time::text").extract_first(),
            'harvestDate': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            'stockTicker': ticker_symbol,
            'index-date': response.css(".mc-info time::text").extract_first(),
            'duplicateGroupId' : 'S' + str(hash(response.url)), #signify it came from scrapy and not lexis
            'languageCode' : response.xpath("/html/@lang").get()
        }
