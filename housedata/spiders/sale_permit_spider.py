# -*- coding: utf-8 -*-
import scrapy
import datetime
from housedata.items import SalePermitItem


class SalePermit(scrapy.Spider):
    # 名字
    name = "salePermit"

    def start_requests(self):
        # 定义爬取的链接
        base_url = "http://www.nnfcxx.com/vipdata/fcj.php?list=xjspf&page="
        nums = 3
        for num in range(1, nums):
            url = base_url + str(num)
            yield scrapy.Request(url=url, callback=self.parse)

    # 分析网页
    def parse(self, response):
        # 取变量
        # 第1列数组
        td_one = response.xpath('//table/tbody/tr/td[1]/text()').extract()
        # 第2列数组
        td_two = response.xpath('//table/tbody/tr/td[2]/text()').extract()
        # 第3列数组
        td_three = response.xpath('//table/tbody/tr/td[3]/text()').extract()
        # 第4列数组
        td_four = response.xpath('//table/tbody/tr/td[4]/text()').extract()
        # 第5列数组
        td_five = response.xpath('//table/tbody/tr/td[5]/text()').extract()
        # 第6列数组
        td_six = response.xpath('//table/tbody/tr/td[6]/text()').extract()

        for i in range(len(td_one)):
            item = SalePermitItem()
            item['companyName'] = td_one[i]
            item['buildingName'] = td_two[i]
            item['buildingLocation'] = td_three[i]
            item['saleNumber'] = td_four[i]
            item['saleArea'] = td_five[i]
            item['approvedTime'] = td_six[i]
            item['createdTime'] = datetime.datetime.now().strftime('%Y-%d-%m %H:%M:%S')
            yield item
