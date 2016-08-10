# -*- coding: utf-8 -*-
import scrapy
from appStore.items import AppstoreItem


class appStoreSpider(scrapy.Spider):
    name = "appStore"
    # allowed_domains = ["https://itunes.apple.com"]
    start_urls = ['https://itunes.apple.com/us/genre/ios/id36?mt=8',]
    def parse(self,response):
        #select category of apps
        #change here:
        for href in response.xpath("//div[@id='genre-nav']/div/ul/li/a/@href")[0].extract():
            yield scrapy.Request(href,callback = self.parse_letter)

    def parse_letter(self,response):
        #select letter of apps
        for href in response.xpath("//div[@id='selectedgenre']/ul/li/a/@href")[0].extract():
            #focus on the first page of each letter
            href = href + "&page=1#page"
            yield scrapy.Request(href,callback = self.parse_letter)


    def parse_category_letter(self, response): 
        #get app data
        for href in response.xpath("//div[@id='selectedcontent']//a/@href").extract():
            yield scrapy.Request(href, callback=self.parse_dir_contents)
        # get link of next page
        next_page = response.xpath("//a[contains(text(),'Next')]/@href")
        #if next page exist , continue
        if next_page: 
            url_next_page = next_page[0].extract() 
            #test
            # print "----------------"
            # print url_next_page
            # print "----------------"
            #recursion
            yield scrapy.Request(url_next_page, self.parse)
        else:
            return
    def parse_dir_contents(self, response):
    	item = AppstoreItem()
    	item['appID'] = response.url.split("/")[-1].split("?")[0][2:]
    	item['name'] = response.xpath("//div[@id='title']/div/h1/text()").extract()
    	item['category'] = response.xpath("//span[@itemprop='applicationCategory']/text()").extract()
    	item['url'] = response.xpath("//meta[@itemprop='image']/@content").extract()
    	item['description'] = response.xpath("//p[@itemprop='description']/text()").extract()
    	item['aggregateRating'] = response.xpath("//div[@class='rating']/span[@itemprop='ratingValue']/text()").extract()
    	item['related_app'] = response.xpath("//div[@class='content']//div[@class='lockup small application']/@adam-id").extract()
    	if response.xpath("//div[@class='extra-list customer-ratings']/div[@class='rating']/@aria-label"):
            item['currentRating'] = response.xpath("//div[@class='extra-list customer-ratings']/div[@class='rating']/@aria-label")[0].extract()
            item['allRating'] = response.xpath("//div[@class='extra-list customer-ratings']/div[@class='rating']/@aria-label")[-1].extract()
    	item['iPhone_screenShot'] = response.xpath("//img[contains(@alt,'iPhone Screenshot')]/@src").extract()
    	item['iPad_screenShot'] = response.xpath("//img[contains(@alt,'iPad Screenshot')]/@src").extract()
    	item['lauch_time'] = response.xpath("//span[@itemprop='datePublished']/text()").extract()
    	return item

