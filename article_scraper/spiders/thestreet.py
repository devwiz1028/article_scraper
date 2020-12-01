# -*- coding: utf-8 -*-
import scrapy
import w3lib.html

class TheStreetSpider(scrapy.Spider):
    name = "thestreet"
    start_urls = [
        "https://thestreet.com/investing"
    ]
    headers= {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'cookie': '__cfduid=d23a5d5d5d9a3ad4c092fe1afb3fee4d71602843384; _pxhd=9304c787f6d4cdc1682462a59c3fc438f262cef619c81b40da673495df174b75:a5225b71-0f98-11eb-8c92-274310408760; adOu=N; at_check=true; AMCVS_56B3E406563CC6B77F000101%40AdobeOrg=1; _gcl_au=1.1.1363953102.1602843392; ajs_anonymous_id=%222bbb1763-5c35-4ff8-80bc-c0a9cbb1ec6b%22; s_ecid=MCMID%7C75238137139771725792235334566105281273; s_cc=true; ibdFV=1; AMCV_56B3E406563CC6B77F000101%40AdobeOrg=-432600572%7CMCIDTS%7C18552%7CvVersion%7C4.5.2%7CMCMID%7C75238137139771725792235334566105281273%7CMCAAMLH-1603448191%7C6%7CMCAAMB-1603448191%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1602850593s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18559; _ga=GA1.2.1177903728.1602843396; _gat=1; _gid=GA1.2.1879479389.1602843396; _pxvid=a5225b71-0f98-11eb-8c92-274310408760; _rdt_uuid=1602843397631.fcb59423-02a8-4c49-9867-6d23f3db2566; amplitude_idundefinedinvestors.com=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; _cb_ls=1; _cb=DO373OC8pPOKDRwbno; _li_dcdm_c=.investors.com; _lc2_fpi=fc5ab248a798--01emrejw5m2bwmxz04kz2qmnev; ibdshcart=40d3b219-7b0b-4e01-8733-1ed81c69a7db; __gads=ID=c1dc0c59204e671d:T=1602843414:S=ALNI_Mbl2nUOVa9G418lyeTCDk3jWzxxVg; QSI_HistorySession=https%3A%2F%2Fwww.investors.com%2Fnews%2Ftechnology%2Fmrna-stock-rises-moderna-advances-covid-19-vaccine-approval-process-europe%2F~1602843435593%7Chttps%3A%2F%2Fnewhome.investors.com%2F%3FmboxSession%3D9a19adb319654f49bb6c7f7dc205b3df%26adobe_mc_sdid%3DSDID%253D5E2E761421C79B92-333A9B30D9F7B1C1%257CMCORGID%253D56B3E406563CC6B77F000101%2540AdobeOrg%257CTS%253D1602843394~1602843454276%7Chttps%3A%2F%2Fwww.investors.com%2Fcategory%2Fnews%2Ftechnology%2F~1602843493750%7Chttps%3A%2F%2Fwww.investors.com%2Fnews%2Ftechnology%2Fisrg-stock-fell-after-intuitive-surgical-again-declines-provide-guidance%2F~1602843762513%7Chttps%3A%2F%2Fwww.investors.com%2Fcategory%2Fnews%2Ftechnology%2F~1602843959174; _parsely_session={%22sid%22:2%2C%22surl%22:%22https://www.investors.com/category/news/technology/%22%2C%22sref%22:%22https://newhome.investors.com/?mboxSession=9a19adb319654f49bb6c7f7dc205b3df&adobe_mc_sdid=SDID%253D5E2E761421C79B92-333A9B30D9F7B1C1%257CMCORGID%253D56B3E406563CC6B77F000101%2540AdobeOrg%257CTS%253D1602843394%22%2C%22sts%22:1602846154159%2C%22slts%22:1602843388133}; _parsely_visitor={%22id%22:%22pid=193bf5b95222329e18d792aab551878b%22%2C%22session_count%22:2%2C%22last_session_ts%22:1602846154159}; ibdVC=2; ua-wn-pv=8; welcome_ad_count=8; s_sq=%5B%5BB%5D%5D; _chartbeat2=.1602843405699.1602847657215.1.B7uNlRCInAL-BK1-VzBKSiG2Bw_Ghd.1; _cb_svref=null; _pxff_bsco=1; _px3=01f95334e83c36c03e6d44a9b2a97476dc3c0dfa61514b1bca136909829c06d7:zbzF/hlcUFLTyX+p89fnknf7Tls/GOJvvKPmD5Idx6o2/h/WM85VgmYa95lY69Cyz4ciyKKc8qRnzCMYZCk0YA==:1000:d0Q2ALxwxc+0tRhz47VjpGSFhDOuNs6dCS9gFfDSu70bDPGudO0sXms+1lmlu+C07JUHjyFcytSoaM3YNwBMmEVm3inLrKjJpv62+LqpE4Ws3Z3XavV0yH1n2IsaEDkKRRTfMEEM5c0J1nHneuVNtT5EL7a7Dvd9BuKhe65s59w=; ibdVS=637384444649085478; mbox=PC#9a19adb319654f49bb6c7f7dc205b3df.38_0#1666092470|session#e20bbe7359e64c09b0a01b2077f90a4e#1602848017; amplitude_id_0bce0d0423742838ad4335ef068a4372investors.com=eyJkZXZpY2VJZCI6ImVhYzViYzBhLTg1ODMtNDk4NC05YzQxLWMxNDY1MTQwYzJlZlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwMjg0NjE2MTUzNCwibGFzdEV2ZW50VGltZSI6MTYwMjg0NzY3MTAwMiwiZXZlbnRJZCI6MjMsImlkZW50aWZ5SWQiOjcsInNlcXVlbmNlTnVtYmVyIjozMH0=; GED_PLAYLIST_ACTIVITY=W3sidSI6IkhaSHoiLCJ0c2wiOjE2MDI4NDc2NzEsIm52IjowLCJ1cHQiOjE2MDI4NDc2NDUsImx0IjoxNjAyODQ3NjQ1fSx7InUiOiI5SmJBIiwidHNsIjoxNjAyODQ3NjY1LCJudiI6MCwidXB0IjoxNjAyODQzNjg4LCJsdCI6MTYwMjg0MzkwOX1d'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        for quote in response.css("phoenix-super-link"):
            url = quote.attrib['href']
            if url.startswith('https://www.thestreet.com/investing'):
                yield scrapy.Request(url, self.parse_article, headers=self.headers)

    def parse_article(self, response):
         yield {
            'Article': response.css("header h1.m-detail-header--title::text").extract_first(),
            'url': response.url,
            'Stock': response.css(".m-detail--body strong a::text").extract_first(),
            'Author': response.css("a.m-detail-header--meta-author::text").extract_first(),
            'Date': response.css(".m-detail-header--date time::text").extract_first(),
            'Analyst Firm': '',
            'Analyst name': '',
            'Content': '\n'.join(map(lambda x: w3lib.html.remove_tags(x).strip(), response.css(".m-detail--body > p").extract()))
        }
