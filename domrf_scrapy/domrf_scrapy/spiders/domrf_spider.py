# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.http import Request
from scrapy.loader import ItemLoader
import json
from domrf_scrapy.items import DomRFItem

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

        domrf_item = ItemLoader(item = DomRFItem(), response = response)

        # article.add_xpath("url", '//meta[@property = "og:url"]/@content')
        domrf_item.add_value('source', "glassdoor")
        domrf_item.add_value('url', response.url)

        domrf_item.add_xpath("job_position", '//div/*[contains(@class, "noMargTop")]/text()')
        domrf_item.add_xpath("job_salary_med", '//meta[@name="description"]/@content')
        domrf_item.add_xpath("job_company", '//meta[@name="description"]/@content')
        domrf_item.add_xpath("job_text", '//div[contains(@class, "jobDescriptionContent")]//*[not(name()="ul") and not(name()="ol") and not(name()="li")]/text()')
        domrf_item.add_xpath("job_text", '//div[contains(@class, "jobDescriptionContent")]/text()')
        domrf_item.add_xpath("job_lists", '//div[contains(@class, "jobDescriptionContent")]//li/text()')
        domrf_item.add_xpath("job_apply_link", '//div[@class = "cell"]/a/@href')
        domrf_item.add_xpath("job_apply_text", '//div[@class = "cell"]/a//text()')

        domrf_item.add_xpath("company_website", '//div[@class = "infoEntity"]//span[@class = "value website"]/a/@href')
        domrf_item.add_xpath("company_size", '//div[@class]/*[contains(text(), "Size")]/following-sibling::span[@class = "value"]/text()')
        domrf_item.add_xpath("company_type", '//div[@class]/*[contains(text(), "Type")]/following-sibling::span[@class = "value"]/text()')
        domrf_item.add_xpath("company_revenue", '//div[@class]/*[contains(text(), "Revenue")]/following-sibling::span[@class = "value"]/text()')
        domrf_item.add_xpath("company_headquarters", '//div[@class]/*[contains(text(), "Headquarters")]/following-sibling::span[@class = "value"]/text()')
        domrf_item.add_xpath("company_founded", '//div[@class]/*[contains(text(), "Founded")]/following-sibling::span[@class = "value"]/text()')
        article.add_xpath("company_industry", '//div[@class]/*[contains(text(), "Industry")]/following-sibling::span[@class = "value"]/text()')
        article.add_xpath("company_description", '//div[@id="EmpBasicInfo"]//div[@data-full]/@data-full')

        article.add_xpath("rating_rating", '//div[@class="empStatsBody"]//div[@class="ratingNum"]/text()')
        article.add_xpath("rating_recommend", '//div[@id="EmpStats_Recommend"]/@data-percentage')
        article.add_xpath("rating_approve", '//div[@id="EmpStats_Approve"]/@data-percentage')

        item = article.load_item()
        yield(item)

        return {#dict
                "developer" : developer,
                #list
                # "developer_data" : developer_data,
                #list
                "developer_group_address" : developer_group_address,
                #dict
                # "developer_report" : developer_report
                }
