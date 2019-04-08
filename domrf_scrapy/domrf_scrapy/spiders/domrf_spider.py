# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.http import Request
from scrapy.loader import ItemLoader
import json
from domrf_scrapy.items import DomRFItem

class DomrfSpiderSpider(scrapy.Spider):
    name = 'domrf_spider'

    custom_settings = {
        "HTTP_PROXY":'http://tor:9050',
        "DOWNLOAD_DELAY": 0,
        # "DOWNLOADER_MIDDLEWARES": {
        #     'myproject.middlewares.RandomUserAgentMiddleware': 400,
        #     'myproject.middlewares.ProxyMiddleware': 410,
        #     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None}
        }
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

        if len(developer_data) > 0:
            for value in developer_data:

                domrf_item = ItemLoader(item = DomRFItem(), response = response)

                # article.add_xpath("url", '//meta[@property = "og:url"]/@content')
                domrf_item.add_value('developer_group_id', developer["developer_group_id"])
                domrf_item.add_value('developer_group_name', developer["developer_group_name"])

                if type(developer_group_address) is list:
                    domrf_item.add_value('developer_group_address', None)
                else:
                    domrf_item.add_value('developer_group_address',
                            developer_group_address['developer_group_address'])

                domrf_item.add_value('region_id', value["region_id"])
                domrf_item.add_value('region_name', value["region_name"])

                domrf_item.add_value('startDate', developer_report["startDate"])
                domrf_item.add_value('endDate', developer_report["endDate"])

                domrf_item.add_value('total_living_floor_size', value["total_living_floor_size"])
                domrf_item.add_value('appt_num', value["appt_num"])
                domrf_item.add_value('object_count', value["object_count"])
                domrf_item.add_value('total_living_floor_size_pct', value["total_living_floor_size_pct"])
                domrf_item.add_value('typed_volume_pct', value["typed_volume_pct"])
                domrf_item.add_value('rating', value["rating"])

                item = domrf_item.load_item()
                yield item

        # return {#dict
        #         # "developer" : developer,
        #         #list
        #         "developer_data" : developer_data,
        #         #list
        #         # "developer_group_address" : developer_group_address,
        #         #dict
        #         # "developer_report" : developer_report
        #         }
