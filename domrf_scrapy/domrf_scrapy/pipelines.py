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

        item["developer_group_id"] = item["developer_group_id"][0]
        item["developer_group_name"] = item["url"][0]
        item["developer_group_address"] = item["url"][0]

        item["region_id"] = item["url"][0]
        item["region_name"] = item["url"][0]

        item["startDate"] = item["url"][0]
        item["endDate"] = item["url"][0]

        item["total_living_floor_size"] = item["url"][0]
        item["appt_num"] = item["url"][0]
        item["object_count"] = item["url"][0]
        item["total_living_floor_size_pct"] = item["url"][0]
        item["typed_volume_pct"] = item["url"][0]
        item["rating"] = item["url"][0]

        return item
