# -*- coding: utf-8 -*-

from scrapy.exporters import JsonItemExporter


class UcimlPipeline(object):
    def __init__(self):
        self.fp = open('uciml_datasets.json', 'wb')
        self.exporter = JsonItemExporter(self.fp, encoding='utf-8')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        for field in item.fields:
            if isinstance(item[field], str):
                item[field] = item[field].strip()
            else:
                item[field] = item[field][0].strip()
        self.exporter.export_item(item)
        return item
   
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()
