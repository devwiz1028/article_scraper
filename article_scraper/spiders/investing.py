# -*- coding: utf-8 -*-
import scrapy
import w3lib.html
import datetime

class InvestingSpider(scrapy.Spider):
    name = "investing"
    start_urls = [
        'https://www.investing.com/news/latest-news',
    ]

    def parse(self, response):
        for quote in response.css(".wrapper #leftColumn article.articleItem a"):
            url = quote.attrib['href']
            yield scrapy.Request('https://www.investing.com' + url, self.parse_article)

    def parse_article(self, response):
        yield {
            'originalUrl' : response.url,
            'url' : response.url, #to match lexis format
            'title': response.css("h1.articleHeader::text").extract_first().strip(),
            'content': '\n'.join(map(lambda x: w3lib.html.remove_tags(x), response.css("div.articlePage p::text").extract())),
            # 'author': {'name': response.css(".article__masthead .article__byline h4::text").extract_first().strip()},
            'category': response.css("div.contentSectionDetails a::text").extract_first().strip(),
            'publishedDate': response.css("div.contentSectionDetails span::text").extract_first().split('(')[1][:-1].strip()
            # 'estimatedPublishedDate': response.css(".article__masthead time.timestamp--pub::text").extract_first().split(':')[1].strip(),
            # 'harvestDate': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            # 'stockTicker': '',
            # 'index-date': response.css(".article__masthead time.timestamp--pub::text").extract_first().split(':')[1].strip(),
            # 'duplicateGroupId' : 'S' + str(hash(response.url)), #signify it came from scrapy and not lexis
            # 'languageCode' : response.xpath("/html/@lang").get()
        }
