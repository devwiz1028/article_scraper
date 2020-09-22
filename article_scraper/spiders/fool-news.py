# -*- coding: utf-8 -*-
import scrapy


class FoolNewsSpider(scrapy.Spider):
    name = "fool-news"
    start_urls = [
        'https://fool.com/investing-news',
    ]

    def parse(self, response):
        for quote in response.css(".recent-articles .article-listing .list-content a"):
            date_author = quote.css(".story-date-author::text").extract_first().split('|')
            yield {
                'originalUrl': 'https://fool.com' + quote.attrib['href'],
                'authorName': date_author[0].strip(),
                'publishedDate': date_author[1].strip(),
                'title': quote.css(".text > h4::text").extract_first(),
                'content': quote.css(".text > p.article-promo::text").extract_first()
            }

        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
