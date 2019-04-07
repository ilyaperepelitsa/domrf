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

        item["url"] = item["url"

        developer_group_id = Field()
        developer_group_name = Field()
        developer_group_address = Field()
        region_id = Field()
        region_name = Field()
        startDate = Field()
        endDate = Field()
        total_living_floor_size = Field()
        appt_num = Field()
        object_count = Field()
        total_living_floor_size_pct = Field()
        typed_volume_pct = Field()
        rating = Field()

        return item
