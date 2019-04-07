# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.http import Request
import json

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
        PR = Request(
            "https://наш.дом.рф/аналитика/grapi/v1/dim_developer_group",
            headers = {"Accept": "json"},

            "Accept": "*/*",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9",
"Connection": "keep-alive"
"content-type": "application/json"


            callback=self.parse_list
        )
        yield PR

    def parse_list(self, response):
        return {"pew" : json.loads(response.body_as_unicode())}
