# -*- coding: utf-8 -*-
import scrapy
import w3lib.html
import datetime

class StockNewsSpider(scrapy.Spider):
    name = "stock-news"
    start_urls = [
        'https://stocknews.com/top-stories',
    ]

    def parse(self, response):
        for quote in response.css("#content .row .col-lg-8.col-md-7 div.margin-bottom h3 a"):
            yield scrapy.Request('https://stocknews.com' + quote.attrib['href'], self.parse_article)

    def parse_article(self, response):
        yield {
            'originalUrl' : response.url,
            'url' : response.url, #to match lexis format
            'title': response.css(".news-event h1.page-title::text").extract_first(),
            'content': w3lib.html.remove_tags(response.css("#articlecontent > p").get()).strip(),
            'author': {'name': response.css(".news-event .panel-body span.post-meta strong a::text").extract_first()[3:]},
            'publishedDate': response.css(".news-event .panel-body span.post-meta ~ a::text").extract_first(),
            'estimatedPublishedDate': response.css(".news-event .panel-body span.post-meta ~ a::text").extract_first(),
            'harvestDate': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            'stockTicker': '',
            'index-date': response.css(".news-event .panel-body span.post-meta ~ a::text").extract_first(),
            'duplicateGroupId' : 'S' + str(hash(response.url)), #signify it came from scrapy and not lexis
            'languageCode' : response.xpath("/html/@lang").get()
        }
