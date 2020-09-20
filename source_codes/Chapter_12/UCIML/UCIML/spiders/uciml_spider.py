# -*- coding: utf-8 -*-

import scrapy
from UCIML.items import DatasetItem


class UcimlSpider(scrapy.Spider):
    name = "uciml"
    start_urls = [
        'https://archive.ics.uci.edu/ml/datasets.php'
    ]
    
    def parse(self, response):
        sel_list = response.xpath('//tr/td/table[@border=1][@cellpadding=5]/tr')[1:]
        for sel in sel_list:            
            name = sel.xpath('td/*//b/a/text()').extract()
            other_cols = sel.xpath('td/p/text()').extract()
            [data_type, default_task, attr_type, instances, attrs, year] = other_cols
            item = DatasetItem()
            item['name'] = name
            item['data_type'] = data_type
            item['default_task'] = default_task,
            item['attr_type'] = attr_type
            item['instances'] = instances,
            item['attrs'] = attrs,
            item['year'] = year
            yield item



    
