# -*- coding: utf-8 -*-
import scrapy

class GoogleNewsSpider(scrapy.Spider):
    name = "google-news"
    start_urls = []
    headers= {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }

    def __init__(self, keyword, pages = 2, *args, **kwargs):
        super(GoogleNewsSpider, self).__init__(*args, **kwargs)
        for page in (1, pages):
            url = 'https://www.google.com/search?q={}&tbm=nws'.format(keyword.replace(' ', '+'))
            if page > 1:
                url += '&start={}'.format((page - 1) * 10)
            self.start_urls.append(url)

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
