# -*- coding: utf-8 -*-
import scrapy
import w3lib.html
import datetime

class GoodReturnsSpider(scrapy.Spider):
    name = "goodreturns"
    start_urls = [
        'https://www.goodreturns.in',
    ]

    def parse(self, response):
        for quote in response.css("div.gd-news-block ul li a"):
            url = quote.attrib['href']
            yield scrapy.Request('https://goodreturns.in' + url, self.parse_article)

    def parse_article(self, response):
        content = ''
        yield {
            'originalUrl' : response.url,
            'url' : response.url, #to match lexis format
            'title': (response.css("article h1.articleheading::text").extract_first() or '').strip(),
            'content': '\n'.join(map(lambda x: w3lib.html.remove_tags(x), response.css("article > div > p::text").extract())),
            'author': {'name': (response.css("article header .date_time a strong::text").extract_first() or '').strip()},
            # 'category': (response.css("div.contentSectionDetails a::text").extract_first() or '').strip(),
            'publishedDate': (response.css("article header .date_time time::text").extract_first().strip()[10:] or '').strip()
            # 'estimatedPublishedDate': response.css(".article__masthead time.timestamp--pub::text").extract_first().split(':')[1].strip(),
            # 'harvestDate': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            # 'stockTicker': '',
            # 'index-date': response.css(".article__masthead time.timestamp--pub::text").extract_first().split(':')[1].strip(),
            # 'duplicateGroupId' : 'S' + str(hash(response.url)), #signify it came from scrapy and not lexis
            # 'languageCode' : response.xpath("/html/@lang").get()
        }
