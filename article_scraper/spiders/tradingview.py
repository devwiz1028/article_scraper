# -*- coding: utf-8 -*-
import scrapy
import w3lib.html
import datetime

class TradingViewSpider(scrapy.Spider):
    name = "tradingview"
    start_urls = [
        'https://www.tradingview.com/markets/world-economy/news',
    ]

    def parse(self, response):
        for quote in response.css("div.js-news-category-page-container.tv-news-category-page-container div:first-child a"):
            url = quote.attrib['href']
            yield scrapy.Request('https://tradingview.com' + url, self.parse_article)

    def parse_article(self, response):
        content = ''
        yield {
            'originalUrl' : response.url,
            'url' : response.url, #to match lexis format
            'title': (response.css("div.paywall article h1::text").extract_first() or '').strip(),
            'content': '\n'.join(map(lambda x: w3lib.html.remove_tags(x), response.css("div.paywall article div:last-child span p::text").extract())),
            'author': {'name': response.css("div.paywall article div:first-child img").attrib['alt'].strip()},
            # 'category': (response.css("div.contentSectionDetails a::text").extract_first() or '').strip(),
            'publishedDate': ' '.join(map(lambda x: w3lib.html.remove_tags(x), response.css("div.paywall article div:nth-child(3) time span::text").extract())),
            # 'estimatedPublishedDate': response.css(".article__masthead time.timestamp--pub::text").extract_first().split(':')[1].strip(),
            # 'harvestDate': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            # 'stockTicker': '',
            # 'index-date': response.css(".article__masthead time.timestamp--pub::text").extract_first().split(':')[1].strip(),
            # 'duplicateGroupId' : 'S' + str(hash(response.url)), #signify it came from scrapy and not lexis
            # 'languageCode' : response.xpath("/html/@lang").get()
        }
