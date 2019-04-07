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
        item["url"] = "".join(item["url"])
        return item
