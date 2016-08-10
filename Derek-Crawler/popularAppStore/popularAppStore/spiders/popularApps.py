# -*- coding: utf-8 -*-
import scrapy
from popularAppStore.items import PopularappstoreItem


class popularAppStoreSpider(scrapy.Spider):
    name = "popularAppStore"
    allowed_domains = ["https://itunes.apple.com"]
    # start_urls = ['https://itunes.apple.com/us/genre/ios-health-fitness/id6013?mt=8',]
    start_urls = ['https://itunes.apple.com/us/genre/ios-books/id6018?mt=8'
,'https://itunes.apple.com/us/genre/ios-business/id6000?mt=8'
,'https://itunes.apple.com/us/genre/ios-catalogs/id6022?mt=8'
,'https://itunes.apple.com/us/genre/ios-education/id6017?mt=8'
,'https://itunes.apple.com/us/genre/ios-entertainment/id6016?mt=8'
,'https://itunes.apple.com/us/genre/ios-finance/id6015?mt=8'
,'https://itunes.apple.com/us/genre/ios-food-drink/id6023?mt=8'
,'https://itunes.apple.com/us/genre/ios-games/id6014?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-action/id7001?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-adventure/id7002?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-arcade/id7003?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-board/id7004?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-card/id7005?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-casino/id7006?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-dice/id7007?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-educational/id7008?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-family/id7009?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-music/id7011?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-puzzle/id7012?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-racing/id7013?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-role-playing/id7014?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-simulation/id7015?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-sports/id7016?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-strategy/id7017?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-trivia/id7018?mt=8'
,'https://itunes.apple.com/us/genre/ios-games-word/id7019?mt=8'
,'https://itunes.apple.com/us/genre/ios-health-fitness/id6013?mt=8'
,'https://itunes.apple.com/us/genre/ios-lifestyle/id6012?mt=8'
,'https://itunes.apple.com/us/genre/ios-magazines-newspapers/id6021?mt=8'
,'https://itunes.apple.com/us/genre/ios-arts-photography/id13007?mt=8'
,'https://itunes.apple.com/us/genre/ios-automotive/id13006?mt=8'
,'https://itunes.apple.com/us/genre/ios-brides-weddings/id13008?mt=8'
,'https://itunes.apple.com/us/genre/ios-business-investing/id13009?mt=8'
,'https://itunes.apple.com/us/genre/ios-childrens-magazines/id13010?mt=8'
,'https://itunes.apple.com/us/genre/ios-computers-internet/id13011?mt=8'
,'https://itunes.apple.com/us/genre/ios-cooking-food-drink/id13012?mt=8'
,'https://itunes.apple.com/us/genre/ios-crafts-hobbies/id13013?mt=8'
,'https://itunes.apple.com/us/genre/ios-electronics-audio/id13014?mt=8'
,'https://itunes.apple.com/us/genre/ios-entertainment/id13015?mt=8'
,'https://itunes.apple.com/us/genre/ios-fashion-style/id13002?mt=8'
,'https://itunes.apple.com/us/genre/ios-health-mind-body/id13017?mt=8'
,'https://itunes.apple.com/us/genre/ios-history/id13018?mt=8'
,'https://itunes.apple.com/us/genre/ios-home-garden/id13003?mt=8'
,'https://itunes.apple.com/us/genre/ios-literary-magazines-journals/id13019?mt=8'
,'https://itunes.apple.com/us/genre/ios-mens-interest/id13020?mt=8'
,'https://itunes.apple.com/us/genre/ios-movies-music/id13021?mt=8'
,'https://itunes.apple.com/us/genre/ios-news-politics/id13001?mt=8'
,'https://itunes.apple.com/us/genre/ios-outdoors-nature/id13004?mt=8'
,'https://itunes.apple.com/us/genre/ios-parenting-family/id13023?mt=8'
,'https://itunes.apple.com/us/genre/ios-pets/id13024?mt=8'
,'https://itunes.apple.com/us/genre/ios-professional-trade/id13025?mt=8'
,'https://itunes.apple.com/us/genre/ios-regional-news/id13026?mt=8'
,'https://itunes.apple.com/us/genre/ios-science/id13027?mt=8'
,'https://itunes.apple.com/us/genre/ios-sports-leisure/id13005?mt=8'
,'https://itunes.apple.com/us/genre/ios-teens/id13028?mt=8'
,'https://itunes.apple.com/us/genre/ios-travel-regional/id13029?mt=8'
,'https://itunes.apple.com/us/genre/ios-womens-interest/id13030?mt=8'
,'https://itunes.apple.com/us/genre/ios-medical/id6020?mt=8'
,'https://itunes.apple.com/us/genre/ios-music/id6011?mt=8'
,'https://itunes.apple.com/us/genre/ios-navigation/id6010?mt=8'
,'https://itunes.apple.com/us/genre/ios-news/id6009?mt=8'
,'https://itunes.apple.com/us/genre/ios-photo-video/id6008?mt=8'
,'https://itunes.apple.com/us/genre/ios-productivity/id6007?mt=8'
,'https://itunes.apple.com/us/genre/ios-reference/id6006?mt=8'
,'https://itunes.apple.com/us/genre/ios-shopping/id6024?mt=8'
,'https://itunes.apple.com/us/genre/ios-social-networking/id6005?mt=8'
,'https://itunes.apple.com/us/genre/ios-sports/id6004?mt=8'
,'https://itunes.apple.com/us/genre/ios-travel/id6003?mt=8'
,'https://itunes.apple.com/us/genre/ios-utilities/id6002?mt=8'
,'https://itunes.apple.com/us/genre/ios-weather/id6001?mt=8']



    def parse(self,response):
        # print response.xpath("//div[@id='genre-nav']//a/@href")[0].extract()
        #select category of apps
        #change here:
        # for href in response.xpath("//div[@id='genre-nav']//a/@href").extract():
            # print "'"+href+"'"
    #         yield scrapy.Request(href,callback = self.parse_category)

    # def parse_category(self, response): 
    #     #get app data
        for href in response.xpath("//div[@id='selectedcontent']//a/@href").extract():
            yield scrapy.Request(href, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
    	item = PopularappstoreItem()
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

