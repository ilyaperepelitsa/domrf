# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class FercItem(scrapy.Item):
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
    object_count = Field()
    appt_num = Field()
    object_count = Field()
    pass
