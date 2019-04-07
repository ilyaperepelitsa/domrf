# -*- coding: utf-8 -*-
import scrapy


class DomrfSpiderSpider(scrapy.Spider):
    name = 'domrf_spider'
    allowed_domains = ['dom.ru']
    start_urls = ['http://dom.ru/']

    def parse(self, response):
        pass
