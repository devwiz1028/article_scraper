# -*- coding: utf-8 -*-
import scrapy
import w3lib.html
import datetime

class NasdaqSpider(scrapy.Spider):
    name = "nasdaq"
    start_urls = [
        'https://nasdaq.com/news-and-insights/topic/markets/world-markets',
        'https://nasdaq.com/news-and-insights/topic/markets/stocks',
    ]

    def parse(self, response):
        for quote in response.css(".content-feed__list a.content-feed__card-title-link"):
            yield scrapy.Request('https://nasdaq.com' + quote.attrib['href'], self.parse_article)

    def parse_article(self, response):
        yield {
            'originalUrl' : response.url,
            'url' : response.url, #to match lexis format
            'title': response.css("h1.article-header__headline span::text").extract_first().strip(),
            'content': '\n'.join(map(lambda x: w3lib.html.remove_tags(x).strip(), response.css(".article-header + .body .body__content > :not(div)").extract())),
            'author': {'name': response.css(".article-header__metadata .byline__author span.byline__name::text").extract_first().strip()},
            'publishedDate': response.css(".article-header__metadata .timestamp time::text").extract_first().strip(),
            'estimatedPublishedDate': response.css(".article-header__metadata .timestamp time::text").extract_first().strip(),
            'harvestDate': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            'stockTicker': '',
            'index-date': response.css(".article-header__metadata .timestamp time::text").extract_first().strip(),
            'duplicateGroupId' : 'S' + str(hash(response.url)), #signify it came from scrapy and not lexis
            'languageCode' : response.xpath("/html/@lang").get()
        }
