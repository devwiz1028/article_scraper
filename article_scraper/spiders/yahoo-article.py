# -*- coding: utf-8 -*-
import scrapy
import datetime

class YahooArticleSpider(scrapy.Spider):
    name = "yahoo-article"
    start_urls = [
        "https://finance.yahoo.com/news/facebook-fb-stock-sinks-market-214509985.html",
        "https://finance.yahoo.com/news/facebook-inc-fb-third-most-224138284.html",
        "https://finance.yahoo.com/news/hedge-funds-think-alphabet-inc-012920701.html",
        "https://finance.yahoo.com/news/alphabet-googl-outpaces-stock-market-214509294.html",
        "https://finance.yahoo.com/news/amazon-amzn-dips-more-broader-214509457.html",
        "https://finance.yahoo.com/news/apple-aapl-dips-more-broader-214509933.html",
        "https://finance.yahoo.com/news/apples-aapl-india-online-store-151603151.html",
        "https://finance.yahoo.com/news/eps-growth-then-check-apple-100208988.html",
        "https://finance.yahoo.com/news/microsoft-msft-stock-sinks-market-214509233.html",
        "https://finance.yahoo.com/news/microsoft-msft-dips-more-broader-214509277.html"
    ]

    def parse(self, response):
        paragraphs = response.css(".caas-body > p *::text").extract()
        content = '\n'.join(map(lambda x: x.strip(), paragraphs))
        yield {
            'originalUrl': response.url,
            'url' : response.url, #to match lexis format
            'title': response.css(".caas-title-wrapper h1::text").extract_first(),
            'content': content,
            'author': {'name': response.css(".caas-attr-meta::text").extract_first()},
            'publishedDate': response.css("time.caas-attr-meta-time::text").extract_first(),
            'estimatedPublishedDate': response.css("time.caas-attr-meta-time::text").extract_first(),
            'harvestDate': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            'stockTicker': '',
            'index-date': response.css("time.caas-attr-meta-time::text").extract_first(),
            'duplicateGroupId' : 'S' + str(hash(response.url)), #signify it came from scrapy and not lexis
            'languageCode' : response.xpath("/html/@lang").get()
        }
