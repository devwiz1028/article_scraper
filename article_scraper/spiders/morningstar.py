# -*- coding: utf-8 -*-
import scrapy
import w3lib.html

class MorningStarSpider(scrapy.Spider):
    name = "morningstar"
    start_urls = [
        "https://www.morningstar.com/markets"
    ]

    def parse(self, response):
        for quote in response.css(".mdc-market-indexes-table--large .mdc-table-body tr"):
            yield {
                'Name': w3lib.html.remove_tags(quote.css("td:nth-child(1) a::text").extract_first()).strip(),
                'Value': w3lib.html.remove_tags(quote.css("td:nth-child(2) span::text").extract_first()).strip(),
                'Graph': w3lib.html.remove_tags(quote.css("td:nth-child(3)::text").extract_first()).strip(),
                'Change': w3lib.html.remove_tags(quote.css("td:nth-child(3)::text").extract_first()).strip(),
                'ChangePercent': w3lib.html.remove_tags(quote.css("td:nth-child(5) span::text").extract_first()).strip(),
                'DateTime': w3lib.html.remove_tags(response.css(".mdc-market-indexes-table__last-updated time::text").extract_first()).strip()
            }
