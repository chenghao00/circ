# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://circ.gov.cn/web/site0/tab5240/module14430/page1.htm']

    # 定义提取url地址规则
    rules = (
        # LinkExtractor 连接提取器，提取url地址
        # callback 提取出来的url地址的response会交给callback处理
        # follow 当前url地址的响应是够重新进过rules来提取url地址，

        # 正则匹配对应的url,提出后交给callback函数
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'), callback='parse_item'),
        # 正则匹配下一页url，follow=true进行翻页
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/module14430/page\d+\.htm'), follow=True),
    )

    def parse_item(self, response):
        item = {}
        # item['title'] = response.xpath('//*[@id="tab_content"]/tbody/tr[1]/td/text()').extract_first()
        # item['public_date'] = response.xpath('//*[@id="tab_content"]/tbody/tr[2]/td/text()[1]').extract_first()
        # # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        item["title"] = re.findall("<!--TitleStart-->(.*?)<!--TitleEnd-->", response.text)[0]
        item["publish_date"] = re.findall("发布时间：(20\d{2}-\d{2}-\d{2})", response.text)[0]
        print(item)
        #return item
        yield scrapy.Request(
            url='',
            callback=self.parse_detail,
            meta={'item':item}
        )

    def parse_detail(self, response):
        item=response.meta['item']
        yield item