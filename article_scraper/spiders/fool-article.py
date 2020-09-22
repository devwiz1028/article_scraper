# -*- coding: utf-8 -*-
import scrapy


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
            'title': response.css(".article-header h1::text").extract_first(),
            'content': response.css(".article-header h2::text").extract_first(),
            'authorName': response.css(".author-name a::text").extract_first(),
            'publishedDate': response.css(".publication-date::text").extract()[1].strip()
        }
