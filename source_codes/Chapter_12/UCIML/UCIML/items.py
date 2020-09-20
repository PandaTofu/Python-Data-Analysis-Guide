# -*- coding: utf-8 -*-

import scrapy


class DatasetItem(scrapy.Item):
    name = scrapy.Field()
    data_type = scrapy.Field()
    default_task = scrapy.Field()
    attr_type = scrapy.Field()
    instances = scrapy.Field()
    attrs = scrapy.Field()
    year = scrapy.Field()
