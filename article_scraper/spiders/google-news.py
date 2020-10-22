# -*- coding: utf-8 -*-
import scrapy

class GoogleNewsSpider(scrapy.Spider):
    name = "google-news"
    start_urls = [
        'https://www.google.com/search?q=FB+stock+news&tbm=nws',
        'https://www.google.com/search?q=FB+stock+news&tbm=nws&start=10',
        # 'https://www.google.com/search?q=GOOGL+stock+news&tbm=nws',
        # 'https://www.google.com/search?q=GOOGL+stock+news&tbm=nws&start=10',
        # 'https://www.google.com/search?q=AAPL+stock+news&tbm=nws',
        # 'https://www.google.com/search?q=AAPL+stock+news&tbm=nws&start=10',
        # 'https://www.google.com/search?q=AMZN+stock+news&tbm=nws',
        # 'https://www.google.com/search?q=AMZN+stock+news&tbm=nws&start=10',
        # 'https://www.google.com/search?q=NFLX+stock+news&tbm=nws',
        # 'https://www.google.com/search?q=NFLX+stock+news&tbm=nws&start=10',
    ]
    headers= {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }

    def parse(self, response):
        urls = []
        for quote in response.css("a"):
            url = quote.attrib['href']
            if url.startswith('/url?q=') and url.find('accounts.google.com') == -1:
                url = url[7:].split('&')[0]
                if url not in urls:
                    urls.append(url)
                    yield {
                        'url': url
                    }
