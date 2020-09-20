# -*- coding: utf-8 -*-

import scrapy


class UcimlSpider(scrapy.Spider):
    name = "uciml"
    start_urls = [
        'https://archive.ics.uci.edu/ml/datasets.php'
    ]

    def parse(self, response):
        with open('datasets.html', 'wb') as fp:
            fp.write(response.body)

