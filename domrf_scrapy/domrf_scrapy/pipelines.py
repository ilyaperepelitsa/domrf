# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from domrf_scrapy.models_psql import *
from sqlalchemy.sql import select
from sqlalchemy import and_
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import exists

class DomrfScrapyPipeline(object):
    def process_item(self, item, spider):

        item["developer_group_id"] = str(item["developer_group_id"][0])
        item["developer_group_name"] = item["developer_group_name"][0]
        item["developer_group_address"] = item["developer_group_address"][0]

        item["region_id"] = str(item["region_id"][0])
        item["region_name"] = item["region_name"][0]

        item["startDate"] = item["startDate"][0]
        item["endDate"] = item["endDate"][0]

        try:
            item["total_living_floor_size"] = int(item["total_living_floor_size"][0])
        except:
            item["total_living_floor_size"] = None

        try:
            item["appt_num"] = int(item["appt_num"][0])
        except:
            item["appt_num"] = None

        try:
            item["object_count"] = int(item["object_count"][0])
        except:
            item["object_count"] = None

        try:
            item["total_living_floor_size_pct"] = float(item["total_living_floor_size_pct"][0])
        except:
            item["total_living_floor_size_pct"] = None

        try:
            item["typed_volume_pct"] = float(item["typed_volume_pct"][0])
        except:
            item["typed_volume_pct"] = None

        try:
            item["rating"] = int(item["rating"][0])
        except:
            item["rating"] = None
        return item


class DeveloperPipeline(object):
    def process_item(self, item, spider):

        developer_entry = {"developer_group_id" : item["developer_group_id"],
                            "developer_group_name" : item["developer_group_name"],
                            "developer_group_address" : item["developer_group_address"]}

        developer_exists = session_test.query(exists().where(and_(
                    Developer.developer_group_id == developer_entry['developer_group_id'],
                    Developer.developer_group_name == developer_entry['developer_group_name'],
                    Developer.developer_group_address == developer_entry['developer_group_address']))).scalar()

        if not developer_exists:
            adding_developer = Developer(**developer_entry)
            session_test.add(adding_developer)
            session_test.commit()

        return item


class RegionPipeline(object):
    def process_item(self, item, spider):

        region_entry = {"region_id" : item["region_id"],
                            "region_name" : item["region_name"]}

        region_exists = session_test.query(exists().where(and_(
                    Region.region_id == region_entry['region_id'],
                    Region.region_name == region_entry['region_name']))).scalar()

        if not region_exists:
            adding_region = Region(**region_entry)
            session_test.add(adding_region)
            session_test.commit()

        return item

class DataPipeline(object):
    def process_item(self, item, spider):

        data_entry = {"developer_group_id" : item["developer_group_id"],
                            "region_id" : item["region_id"],
                            "startDate" : item["startDate"],
                            "endDate" : item["endDate"],
                            "total_living_floor_size" : item["total_living_floor_size"],
                            "appt_num" : item["appt_num"],
                            "object_count" : item["object_count"],
                            "total_living_floor_size_pct" : item["total_living_floor_size_pct"],
                            "typed_volume_pct" : item["typed_volume_pct"],
                            "rating" : item["rating"]}

        data_exists = session_test.query(exists().where(and_(
                    DeveloperData.developer_group_id == data_entry['developer_group_id'],
                    DeveloperData.region_id == data_entry['region_id'],
                    DeveloperData.startDate == data_entry['startDate'],
                    DeveloperData.endDate == data_entry['endDate']
                    ))).scalar()

        if not data_exists:
            adding_data = DeveloperData(**data_entry)
            session_test.add(adding_data)
            session_test.commit()

        return item
