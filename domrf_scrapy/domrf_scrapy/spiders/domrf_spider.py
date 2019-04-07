# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.http import Request
import json

class DomrfSpiderSpider(scrapy.Spider):
    name = 'domrf_spider'
    # allowed_domains = ['наш.дом.рф']
    start_urls = ['https://наш.дом.рф/аналитика/grapi/v1/dim_developer_group']
    headers = {"Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "content-type": "application/json"}
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
            headers = self.headers,
            callback=self.parse_list
        )
        return PR

    def parse_list(self, response):
        for developer in json.loads(response.body_as_unicode()):
            developer_details_request =  Request(
                "https://наш.дом.рф/аналитика/grapi/v1/developer_group_region?developerGroupId={developer_id}".format(**{"developer_id" : developer["developer_group_id"]}),
                meta={'developer': developer},
                headers = self.headers,
                callback=self.parse_developer_detailed
            )
            yield developer_details_request

        # return {"pew" : json.loads(response.body_as_unicode())}

    def parse_developer_detailed(self, response):

        developer = response.meta['developer']
        developer_data = json.loads(response.body_as_unicode())

        alt_details_request =  Request(
            "https://наш.дом.рф/аналитика/grapi/v1/developer_group_info?developerGroupId={developer_id}".format(**{"developer_id" : developer["developer_group_id"]}),
            meta={'developer': developer,
                    'developer_data': developer_data},
            headers = self.headers,
            callback=self.parse_alt_details
        )
        yield alt_details_request


    def parse_alt_details(self, response):

        developer = response.meta['developer']
        developer_data = response.meta['developer_data']
        developer_group_address = json.loads(response.body_as_unicode())

        report_data_request =  Request(
            "https://наш.дом.рф/аналитика/grapi/v1/entityInfoDateRange?id={developer_id}&type=devGroup".format(**{"developer_id" : developer["developer_group_id"]}),
            meta={'developer': developer,
                    'developer_data': developer_data,
                    'developer_group_address' : developer_group_address},
            headers = self.headers,
            callback=self.parse_developer_report
        )
        yield report_data_request

    def parse_developer_report(self, response):

        developer = response.meta['developer']
        developer_data = response.meta['developer_data']
        developer_group_address = response.meta['developer_group_address']
        developer_report = json.loads(response.body_as_unicode())["payload"]

        return {#dict
                "developer" : type(developer),
                #list
                "developer_data" : type(developer_data),
                #list
                "developer_group_address" : type(developer_group_address),
                "developer_report" : type(developer_report)}
