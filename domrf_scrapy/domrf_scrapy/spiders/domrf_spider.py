# -*- coding: utf-8 -*-
import scrapy


class DomrfSpiderSpider(scrapy.Spider):
    name = 'domrf_spider'
    allowed_domains = ['наш.дом.рф']
    start_urls = ['https://наш.дом.рф/аналитика/grapi/v1/dim_developer_group']

    def parse(self, response):
        yield response
