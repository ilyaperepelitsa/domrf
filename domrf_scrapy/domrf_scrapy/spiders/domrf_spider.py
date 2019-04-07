# -*- coding: utf-8 -*-
import scrapy


class DomrfSpiderSpider(scrapy.Spider):
    name = 'domrf_spider'
    allowed_domains = ['наш.дом.рф']
    start_urls = ['https://наш.дом.рф/аналитика/grapi/v1/dim_developer_group']
    # PR = Request(
    #     "https://наш.дом.рф/аналитика/grapi/v1/dim_developer_group",
    #     callback=self.parse_PR
    # )
    # return PR
    #
    # def parse(self, response):
    #
    #     PR = Request(
    #         "https://наш.дом.рф/аналитика/grapi/v1/dim_developer_group",
    #         # headers=self.headers,
    #         # meta={'newrequest': Request('htp//sitetoscrape.com',  headers=self.headers),},
    #         callback=self.parse_PR
    #     )
    #     yield PR

    def parse(self, response):
        proxy_data = get_data_from_response(PR)
        yield {"data" : proxy_data}
