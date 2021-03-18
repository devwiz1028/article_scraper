# -*- coding: utf-8 -*-
import scrapy

class InvestorHangoutSpider(scrapy.Spider):
    name = "investor-hangout"
    start_urls = [
        "https://investorhangout.com/whatshot/activeboard"
    ]

    def parse(self, response):
        for row in response.css("table.items tbody tr"):
            yield {
                'name': row.css("td:nth-child(1) a::text").extract_first(),
                'content': row.css("td:nth-child(2) a::text").extract_first(),
                'author': row.css("td:nth-child(3) a::text").extract_first(),
                'createdAt': row.css("td:nth-child(4)::text").extract_first()
            }
