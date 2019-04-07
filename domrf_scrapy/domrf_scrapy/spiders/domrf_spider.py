# -*- coding: utf-8 -*-
import scrapy


class DomrfSpiderSpider(scrapy.Spider):
    name = 'domrf_spider'
    # allowed_domains = ['наш.дом.рф']
    # start_urls = ['https://наш.дом.рф/аналитика/grapi/v1/dim_developer_group']

    def parse(self, response):

        PR = Request(
            "https://наш.дом.рф/аналитика/grapi/v1/dim_developer_group",
            # headers=self.headers,
            # meta={'newrequest': Request('htp//sitetoscrape.com',  headers=self.headers),},
            callback=self.parse_PR
        )
        yield PR

    def parse(self, response):
        
