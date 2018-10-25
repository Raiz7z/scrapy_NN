# -*- coding: utf-8 -*-
import json
from pymongo import MongoClient

from housedata.items import SalePermitItem


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HousedataPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWritePipeline(object):
    def __init__(self):
        self.file = open('items.jl', 'w')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item


class InsertMongodbPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client['house_data']

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)
        self.db
