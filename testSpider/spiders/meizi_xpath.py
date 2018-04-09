# -*- coding: utf-8 -*-

import scrapy

from testSpider.items import MeiZiItem

# spiders instead of spider
class MeiZiSpider(scrapy.spiders.Spider): 
    name = "meizi"
    allowed_domains = ["meizi.org"]
    # start_urls = [
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    # ]
    start_urls = [
        "http://www.meizitu.com/a/5530.html",
        "http://www.meizitu.com/a/5585.html"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@id="picture"]'):
            item = MeiZiItem()
            item['text'] = sel.xpath('./p/img/@alt').extract()
            item['url'] = sel.xpath('./p/img/@src').extract()
            yield item

        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
