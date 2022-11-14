# -*- coding: utf-8 -*-
import scrapy
import w3lib.html
import datetime

class EconomicTimesSpider(scrapy.Spider):
    name = "economictimes"
    start_urls = [
        'https://economictimes.indiatimes.com/news/latest-news',
    ]

    def parse(self, response):
        for quote in response.css("ul.data li a"):
            url = quote.attrib['href']
            yield scrapy.Request('https://economictimes.indiatimes.com' + url, self.parse_article)

    def parse_article(self, response):
        content = ''
        yield {
            'originalUrl' : response.url,
            'url' : response.url, #to match lexis format
            'title': (response.css("h1.artTitle::text").extract_first() or '').strip(),
            'content': '\n'.join(map(lambda x: w3lib.html.remove_tags(x), response.css("div.pageContent div.artText::text").extract())),
            'author': {'name': (response.css("div.bylineBox span.ag::text").extract_first() or '').strip()},
            # 'category': (response.css("div.contentSectionDetails a::text").extract_first() or '').strip(),
            'publishedDate': (response.css("div.bylineBox time::text").extract_first()[14:] or '').strip()
            # 'estimatedPublishedDate': response.css(".article__masthead time.timestamp--pub::text").extract_first().split(':')[1].strip(),
            # 'harvestDate': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            # 'stockTicker': '',
            # 'index-date': response.css(".article__masthead time.timestamp--pub::text").extract_first().split(':')[1].strip(),
            # 'duplicateGroupId' : 'S' + str(hash(response.url)), #signify it came from scrapy and not lexis
            # 'languageCode' : response.xpath("/html/@lang").get()
        }
