# -*- coding: utf-8 -*-
import scrapy


class DomrfSpiderSpider(scrapy.Spider):
    name = 'domrf_spider'
    # allowed_domains = ['наш.дом.рф']
    # start_urls = ['https://наш.дом.рф/аналитика/grapi/v1/dim_developer_group']

    def parse(self, response):
        # yield {"pew" : dir(response)}
        def parse(self, response):
    for i in range(1,3,1):
        PR = Request(
            'http://myproxyapi.com',
            headers=self.headers,
            meta={'newrequest': Request('htp//sitetoscrape.com',  headers=self.headers),},
            callback=self.parse_PR
        )
        yield PR
