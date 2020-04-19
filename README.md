# circ
Scrapy中CrawlSpider类


1、scrapy genspider –t crawl 爬虫名 “域名”

2、不再有parse方法，被用做基础

3、LinkExtractor 连接提取器，提取url地址；callback 提取出来的url地址的response会交给callback处理；follow 当前url地址的响应是够重新进过rules来提取url地址，

4、不指定callback函数的请求下，若follow为True，满足该Rule的url还会被继续请求

5、若多个Rule都满足一个url，会选择第一个满足的条件 即rules=（Rule（），）是元组，有序
