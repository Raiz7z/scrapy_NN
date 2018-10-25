# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SalePermitItem(scrapy.Item):
    companyName = scrapy.Field()
    buildingName = scrapy.Field()
    buildingLocation = scrapy.Field()
    saleNumber = scrapy.Field()
    saleArea = scrapy.Field()
    approvedTime = scrapy.Field()
    createdTime = scrapy.Field()
    pass
