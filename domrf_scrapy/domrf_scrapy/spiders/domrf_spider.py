# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.http import FormRequest


class DomrfSpiderSpider(scrapy.Spider):
    name = 'domrf_spider'
    # allowed_domains = ['наш.дом.рф']
    start_urls = ['https://наш.дом.рф/аналитика/grapi/v1/dim_developer_group']

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
        PR = FormRequest(
            "https://наш.дом.рф/аналитика/grapi/v1/dim_developer_group",
            callback=self.parse_list
        )
        yield PR

    def parse_list(self, response):
        return response.headers
