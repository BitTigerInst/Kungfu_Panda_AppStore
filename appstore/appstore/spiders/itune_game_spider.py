import scrapy
import re
from scrapy.selector import Selector
from appstore.items import AppstoreItem

class ItunesGameSpider(scrapy.Spider):
    name = "ItunesGame"
    allowed_domains = ["apple.com"]

    start_urls = [
        "http://itunes.apple.com/us/genre/ios-games/id6014?mt=8"
    ]
 
    def parse(self, response):
        page = Selector(response)
        divs = page.xpath('//*[@id="selectedcontent"]/div/ul/li/a')

        for div in divs:
            item = AppstoreItem()
            item['title'] = div.xpath('./text()').extract_first().encode('utf-8')
            item['url'] = div.xpath('./@href').extract_first()
            appid = re.match(r'https://.*/(.*)\?mt=8$', item['url']).group(1)
            item['appid'] = appid 
            #item['intro'] = div.xpath('.//p[@class="content"]/text()').extract_first().encode('utf-8')
            yield item
