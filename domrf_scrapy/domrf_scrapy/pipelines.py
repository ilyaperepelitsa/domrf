# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from news.models import *
from sqlalchemy.sql import select
from sqlalchemy import and_
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import exists

class DomrfScrapyPipeline(object):
    def process_item(self, item, spider):

        item["developer_group_id"] = int(item["developer_group_id"][0])
        item["developer_group_name"] = item["developer_group_name"][0]
        item["developer_group_address"] = item["developer_group_address"][0]

        item["region_id"] = int(item["region_id"][0])
        item["region_name"] = item["region_name"][0]

        item["startDate"] = item["startDate"][0]
        item["endDate"] = item["endDate"][0]

        item["total_living_floor_size"] = int(item["total_living_floor_size"][0])
        item["appt_num"] = int(item["appt_num"][0])
        item["object_count"] = int(item["object_count"][0])
        item["total_living_floor_size_pct"] = float(item["total_living_floor_size_pct"][0])
        item["typed_volume_pct"] = float(item["typed_volume_pct"][0])
        item["rating"] = int(item["rating"][0])

        yield item


class DeveloperPipeline(object):
    def process_item(self, item, spider):

        developer_entry = {"url" : item["url"],
                            "url" : item["url"],
                            "url" : item["url"]}

        url_exists = session_test.query(exists().where(Url_entry.url==item["url"])).scalar()
        if not url_exists:
            adding_url = Url_entry(**url_entry)
            session_test.add(adding_url)
            session_test.commit()

        yield item


class RegionPipeline(object):
    def process_item(self, item, spider):


        yield item

class DataPipeline(object):
    def process_item(self, item, spider):


        yield item
