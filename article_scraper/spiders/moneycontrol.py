# -*- coding: utf-8 -*-
import scrapy
import w3lib.html
import datetime

class MoneyControlSpider(scrapy.Spider):
    name = "moneycontrol"
    start_urls = [
        'https://www.moneycontrol.com/news/fintech',
    ]

    def parse(self, response):
        for quote in response.css(".expertitem .item a"):
            url = quote.attrib['href']
            if (url != 'https://www.moneycontrol.com/'):
                yield scrapy.Request(url, self.parse_article)

    def parse_article(self, response):
        content = ''
        yield {
            'originalUrl' : response.url,
            'url' : response.url, #to match lexis format
            'title': (response.css("h1.article_title::text").extract_first() or '').strip(),
            'content': '\n'.join(map(lambda x: w3lib.html.remove_tags(x), response.css("div.content_wrapper p::text").extract())),
            'author': {'name': (response.css("div.article_author a::text").extract_first() or '').strip()},
            # 'category': (response.css("div.contentSectionDetails a::text").extract_first() or '').strip(),
            'publishedDate': (response.css("div.article_schedule span::text").extract_first() or '').strip()
            # 'estimatedPublishedDate': response.css(".article__masthead time.timestamp--pub::text").extract_first().split(':')[1].strip(),
            # 'harvestDate': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            # 'stockTicker': '',
            # 'index-date': response.css(".article__masthead time.timestamp--pub::text").extract_first().split(':')[1].strip(),
            # 'duplicateGroupId' : 'S' + str(hash(response.url)), #signify it came from scrapy and not lexis
            # 'languageCode' : response.xpath("/html/@lang").get()
        }
