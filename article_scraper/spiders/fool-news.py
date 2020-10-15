# -*- coding: utf-8 -*-
import scrapy
import w3lib.html
import datetime

class FoolNewsSpider(scrapy.Spider):
    name = "fool-news"
    allowed_domains = ['fool.com'] #so we don't stray elsewhere
    start_urls = [
        'https://fool.com/investing-news',
    ]



    def parse(self, response):
        for quote in response.css(".recent-articles .article-listing .list-content a"):
            date_author = quote.css(".story-date-author::text").extract_first().split('|')

            yield scrapy.Request('https://fool.com' + quote.attrib['href'], self.parse_article)

    def parse_article(self, response):
        yield {
            'originalUrl' : response.url,
            'url' : response.url, #to match lexis format
            'title': response.css(".article-header h1::text").extract_first(),
            'content': w3lib.html.remove_tags(response.css(".article-content").get()).strip(),
            'author': {'name': response.css(".author-name a::text").extract_first()},
            'publishedDate': response.xpath("//meta[@name='date']/@content").get(),
            'estimatedPublishedDate': response.xpath("//meta[@name='date']/@content").get(),
            'harvestDate': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            'stockTicker': response.xpath("//meta[@name='tickers']/@content").get(),
            'index-date': response.xpath("//meta[@name='date']/@content").get(),
            'duplicateGroupId' : 'S' + str(hash(response.url)), #signify it came from scrapy and not lexis
            'index-date' : response.xpath("//meta[@name='date']/@content").get()[:10],
            'languageCode' : response.xpath("/html/@lang").get()
        }
