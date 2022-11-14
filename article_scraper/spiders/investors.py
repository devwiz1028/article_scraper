# -*- coding: utf-8 -*-
import scrapy
import w3lib.html
import datetime
import json

class InvestorsSpider(scrapy.Spider):
    name = "investors"
    start_urls = [
        'https://www.investors.com/wp-admin/admin-ajax.php?slug=technology&posts_per_page=20&post_type=post&repeater=default&preloaded=false&preloaded_amount=0&category=technology&order=DESC&orderby=date&action=alm_get_posts&query_type=standard',
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'cookie': 'adOu=N; _cb=DP5dlA61t4BBej8Bd; _rdt_uuid=1664090553312.c9704a95-010a-4156-9ee3-2e2b14dcf9e2; _pxvid=d1ea24c2-3ca2-11ed-b377-4945454d734c; gig_bootstrap_3_H1yN9UVDBc6ix9wBEAvcnQORVTJ5gA5vgWv_FrEQ9Xijk0CNrVuU6YRjWz2zHZAe=login_ver4; _pxhd=9xDLzPjNWip4rmMkqFFqwsP/V9PsQMzgRT6A6dyv1XxlVIwVvnPQZDmw0tURBbkftCvr8/5pWp93Kzd8ufuOwg==:vaOLPcGxLD8SJxTCMnOgbwRqcs8H00RnhFpC1zpWWB8IaVm1GJoBavJoK0MzT96j9gzGXEp1eqRM3o6pHJGAEn3AYxvWrI504Z8KXlyUs4Q=; at_check=true; AMCVS_56B3E406563CC6B77F000101%40AdobeOrg=1; _gcl_au=1.1.985504821.1668442136; s_ecid=MCMID%7C71598652192551984083674628233637571520; AMCV_56B3E406563CC6B77F000101%40AdobeOrg=-127034327%7CMCIDTS%7C19311%7CMCMID%7C71598652192551984083674628233637571520%7CMCAAMLH-1669046934%7C7%7CMCAAMB-1669046934%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1668449337s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.1.0; s_cc=true; _gid=GA1.2.1470118822.1668442143; _scid=24e64aef-c828-4a02-8bf5-0bc9b14a19ef; pxcts=a914b68e-6436-11ed-91f6-69454b4a4f4e; ln_or=d; _li_dcdm_c=.investors.com; _lc2_fpi=fc5ab248a798--01ghvedjtbqnhvx7m5p357j97a; cto_bundle=LtbORl9vTkFIcUhrZVdOUVd3d1hyajBOek5wa1ZSZzZiOGo5Qk1PWFVLcEVNMk51ZEo1eDBXbEo3NDExTjg0VmdCNEpFemExNGZPZENjUXJPODBzU0JvRzVCQTZiMEslMkJGZ0ZUZGRuTVNtWlBuZDN3YiUyRnFFYk5yNEIzcWRyQWd6YU9BRHRXVEJ2QmpTNkpxUWZqd21uaUFYMjd3JTNEJTNE; ibdshcart=d1076883-e556-4c5e-b3d0-ab301a90ee4c; QSI_SI_b3B9jsfbYnFoklL_intercept=true; ibdFV=1; _parsely_visitor={%22id%22:%22pid=e411f11acea9f21fcd09807e72c0dbc7%22%2C%22session_count%22:2%2C%22last_session_ts%22:1668446836809}; ibdVC=4; ibdVS=638040437073239817; mbox=PC#c32da36da87044d0b2089fcacba0e909.34_0#1731691710|session#3862adfa316045069c9b81f85f0194db#1668448700; ua-wn-pv=3; welcome_ad_count=3; _ga_39H8R0813Z=GS1.1.1668446837.2.1.1668446909.0.0.0; _ga=GA1.1.1482150343.1668442143; s_sq=%5B%5BB%5D%5D; _chartbeat2=.1664090534239.1668446909951.0000000000000001.ClZoEdD1vGnwCP9-ESBBPNrwCWlWHt.2; _uetsid=aa10ba60643611ed93544bfc77bc6822; _uetvid=d4d2ce903ca211ed8f6dc978c4f7df0d; permutive-id=29bc3c8f-dcfb-4128-b778-1bdc0b9aaa49; QSI_HistorySession=https%3A%2F%2Fwww.investors.com%2Ftechnology%2F~1668442181913%7Chttps%3A%2F%2Fwww.investors.com%2Fnews%2Ftechnology%2Fbiogen-stock-surges-after-roche-alzheimers-treatment-flops-in-phase-3%2F~1668446923265; _px3=46d9e3f3363f8b81bc392245a4ac677f883dcf32435cd8627547e84dae83aca7:WRZEDrByLbQXh32J76uRqsavVYIegMVPT4wuSrASNHmOtkOu2hMnnShcvCemHprmH1Q3S8MRGQkmRKPGiZb5aw==:1000:v9rgE5BJ+dnqR/HJQC8nyJ8ZKzrxP7+p7aCcJG01ZrXI+5nknz0ZRLHh8Xh/W5iSbBr/QaRVoXI7tf8nx0qtazmdN4iufwGAc7i44bVTlTHu5D37yZjt6OxvCFih11+yFIXqKf7u9Z+SRnNAYEpDQ3+z1Z+DBxjdBrtfgUVhe0yrKsenDqZWyukq2TV4fXcNFVpwbWCEvrTT4Ul2XVb2fg=='
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'cookie': '_pxhd=FOmrk2UsON/MjhpcF704Eo/A5i-9iLS2D5om4iONXDjNTSQWEfIA8bsQKaxhWsFOHcNxn9pkg8mkdR69tYuXPw==:FI31sHObWGOs9ZE581d4hbOjUh6ItgVRVQ9z8oopUQlcdWGMOEBOh0vxverp2qDTolv4zhwfIHMcNRXMaY6B2jXhZLpShvIVw2RLDHh/eas=; _pxff_cc=U2VjdXJlOw==; pxcts=8d939f12-6451-11ed-9485-43677854436f; _pxvid=8b1229d0-6451-11ed-9536-694367755978; _pxff_rf=1; _pxff_fp=1; _pxff_bsco=1; _px3=c4b84cf92775680ee20a3b96d66b081a61f10b85a1fac36c24d4ad5567409a6d:qW5T1PLq6/y6WksMkZn3BKnkrG25dTPL24ZCuO3ZCxcukQxoe171OZ53Sw+SDnyUjqZkMr7kbGhG93Z3XEqphA==:1000:aS0VOGJVfC+HQf6y4Etr9xDzHhMXMNspdNebIS/t3yq6jgLdYAQS71QiaBk+nIuO1iNpS2ZsxDeVNZu1mB/3q4pDt7eIs+nSs1vDFYrvcbFYrx0QXN3gd7kFwgsUfU7fZobKtb0c3jVksVfkd6ArMBEs+cPITnxAX4BPGNmOFwypcctce5srlJ+G3lDUDlDlca7ldzKN8Oguh0mpxypFKA==; adOu=N; ibdVC=1; ibdVS=638040505132377181; at_check=true; ua-wn-pv=1; welcome_ad_count=1; permutive-id=79e3a06c-d603-4176-b336-6db21c71795f; AMCVS_56B3E406563CC6B77F000101%40AdobeOrg=1; mbox=session#fa7a46fafc994481b027480b97d65ee3#1668455576|PC#fa7a46fafc994481b027480b97d65ee3.34_0#1731698520; s_ecid=MCMID%7C47761653922966689304576067706199297994; _gcl_au=1.1.1508874442.1668453721; s_visit=1; s_cc=true; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.investors.com/news/technology/looking-for-company-with-model-chart-check-out-model-n-stock/%22%2C%22sref%22:%22https://www.investors.com/news/technology/looking-for-company-with-model-chart-check-out-model-n-stock%22%2C%22sts%22:1668453722352%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=6eaecd202efa0b59f5dc1fc607e27117%22%2C%22session_count%22:1%2C%22last_session_ts%22:1668453722352}; ibdshcart=85ac21d2-dfea-498a-a48f-de332e6676a0; __gads=ID=69f0d0eb0a1910ff:T=1668453722:S=ALNI_MZcKRB0gtbcrnbkfOj3LC70XWodwg; __gpi=UID=000008a9131c1267:T=1668453722:RT=1668453722:S=ALNI_MYks-G4GOHDageHi8HUu_QirglFlw; AMCV_56B3E406563CC6B77F000101%40AdobeOrg=-127034327%7CMCIDTS%7C19311%7CMCMID%7C47761653922966689304576067706199297994%7CMCAAMLH-1669058517%7C7%7CMCAAMB-1669058517%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1668460919s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19318%7CvVersion%7C5.1.0; ibdFV=1'
        }
        json_data = json.loads(response.text)
        html_text = json_data['html']
        response = scrapy.selector.Selector(text=html_text)
        for quote in response.css("li h3 a"):
            yield scrapy.Request(quote.attrib['href'], self.parse_article, headers=headers)

    def parse_article(self, response):
        yield {
            'originalUrl' : response.url,
            'url' : response.url, #to match lexis format
            'title': response.css("header h1::text").extract_first(),
            'content': '\n'.join(map(lambda x: w3lib.html.remove_tags(x).strip(), response.css(".single-post-content > p, .single-post-content > h2").extract())),
            'author': {'name': response.css("header .post-meta a::text").extract_first()},
            'publishedDate': response.css("header .post-time::text").extract_first(),
            'estimatedPublishedDate': response.css("header .post-time::text").extract_first(),
            'harvestDate': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            'stockTicker': '',
            'index-date': response.css("header .post-time::text").extract_first(),
            'duplicateGroupId' : 'S' + str(hash(response.url)), #signify it came from scrapy and not lexis
            'languageCode' : response.xpath("/html/@lang").get()
        }
