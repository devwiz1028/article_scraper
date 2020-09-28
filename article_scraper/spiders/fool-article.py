# -*- coding: utf-8 -*-
import scrapy
import w3lib.html

class FoolArticleSpider(scrapy.Spider):
    name = "fool-article"
    start_urls = [
        "https://www.fool.com/investing/2020/08/26/why-facebook-stock-surged-to-a-new-all-time-high-t/",
        "https://www.fool.com/investing/2020/09/14/4-unstoppable-stocks-to-buy-with-2500/",
        "https://www.fool.com/investing/2020/09/19/will-amazon-split-its-stock/",
        "https://www.fool.com/investing/2020/09/17/amazons-gearing-up-for-a-massive-q4/",
        "https://www.fool.com/investing/2020/09/17/2-stocks-you-can-keep-forever/",
        "https://www.fool.com/investing/2020/09/16/apple-stock-will-soar-24-to-140-according-to-this/",
        "https://www.fool.com/investing/2020/09/17/why-investors-should-love-microsofts-dividend/",
        "https://www.fool.com/investing/2020/09/16/microsoft-boosts-dividend-by-10/"
    ]

    def parse(self, response):
         yield {
            'originalUrl' : response.url,
            'url' : response.url, #to match lexis format
            'title': response.css(".article-header h1::text").extract_first(),
            'content': w3lib.html.remove_tags(response.css(".article-content").get()).strip(),
            'authorName': response.css(".author-name a::text").extract_first(),
            'publishedDate': response.xpath("//meta[@name='date']/@content").get(),
            'harvestDate': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            'stockTicker': response.xpath("//meta[@name='tickers']/@content").get(),
            'duplicateGroupId' : 'S' + str(hash(response.url)), #signify it came from scrapy and not lexis
            'index-date' : response.xpath("//meta[@name='date']/@content").get()[:10],
            'languageCode' : response.xpath("/html/@lang").get()
            }
