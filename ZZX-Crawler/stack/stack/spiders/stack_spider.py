#from scrapy.spider import CrawlSpider
#from scrapy.selector import Selector
#from stack.items import StackItem

#class StackSpider(CrawlSpider):
#    name="stack"
#    allowed_domains=["web.stanford.edu"]
#    start_urls=["http://web.stanford.edu/class/cs276/"]
#def parse(self,response):
#    chapters=response.xpath('/html/body/div[2]/div/table/tr[2]')
#    for chapter in chapters:
#        item=StackItem()
#        str=chapter.xpath('td[3]/text()').extract()[0]
#        item['title']="title"
#        item['category']="cate"
#        item['url']="url"
#        
#        yield item

import scrapy
import re

from linklist import linkslist
from stack.items import StackItem


class DmozSpider(scrapy.Spider):
    name = "stack"
    allowed_domains = ["itunes.apple.com"]
    start_urls=['https://itunes.apple.com/us/genre/ios-books/id6018?mt=8',
                'https://itunes.apple.com/us/genre/ios-business/id6000?mt=8',
                'https://itunes.apple.com/us/genre/ios-catalogs/id6022?mt=8',
                'https://itunes.apple.com/us/genre/ios-education/id6017?mt=8',
                'https://itunes.apple.com/us/genre/ios-entertainment/id6016?mt=8',
                'https://itunes.apple.com/us/genre/ios-finance/id6015?mt=8',
                'https://itunes.apple.com/us/genre/ios-food-drink/id6023?mt=8',
                'https://itunes.apple.com/us/genre/ios-games-action/id7001?mt=8',
                'https://itunes.apple.com/us/genre/ios-games-adventure/id7002?mt=8',
                'https://itunes.apple.com/us/genre/ios-games-arcade/id7003?mt=8',
                'https://itunes.apple.com/us/genre/ios-games-board/id7004?mt=8',
                'https://itunes.apple.com/us/genre/ios-games-card/id7005?mt=8',
                'https://itunes.apple.com/us/genre/ios-games-casino/id7006?mt=8',
                'https://itunes.apple.com/us/genre/ios-games-dice/id7007?mt=8',
                'https://itunes.apple.com/us/genre/ios-games-educational/id7008?mt=8',
                'https://itunes.apple.com/us/genre/ios-games-family/id7009?mt=8',
               'https://itunes.apple.com/us/genre/ios-games-music/id7011?mt=8',
               'https://itunes.apple.com/us/genre/ios-games-puzzle/id7012?mt=8',
               'https://itunes.apple.com/us/genre/ios-games-racing/id7013?mt=8',
               'https://itunes.apple.com/us/genre/ios-games-role-playing/id7014?mt=8',
               'https://itunes.apple.com/us/genre/ios-games-simulation/id7015?mt=8',
               'https://itunes.apple.com/us/genre/ios-games-sports/id7016?mt=8',
               'https://itunes.apple.com/us/genre/ios-games-strategy/id7017?mt=8',
               'https://itunes.apple.com/us/genre/ios-games-trivia/id7018?mt=8',
               'https://itunes.apple.com/us/genre/ios-games-word/id7019?mt=8',
               'https://itunes.apple.com/us/genre/ios-health-fitness/id6013?mt=8',
               'https://itunes.apple.com/us/genre/ios-lifestyle/id6012?mt=8',
               'https://itunes.apple.com/us/genre/ios-magazines-newspapers/id6021?mt=8',
               'https://itunes.apple.com/us/genre/ios-medical/id6020?mt=8',
               'https://itunes.apple.com/us/genre/ios-music/id6011?mt=8',
               'https://itunes.apple.com/us/genre/ios-navigation/id6010?mt=8',
               'https://itunes.apple.com/us/genre/ios-news/id6009?mt=8',
               'https://itunes.apple.com/us/genre/ios-photo-video/id6008?mt=8',
               'https://itunes.apple.com/us/genre/ios-productivity/id6007?mt=8',
               'https://itunes.apple.com/us/genre/ios-reference/id6006?mt=8',
               'https://itunes.apple.com/us/genre/ios-shopping/id6024?mt=8',
               'https://itunes.apple.com/us/genre/ios-social-networking/id6005?mt=8',
               'https://itunes.apple.com/us/genre/ios-sports/id6004?mt=8',
               'https://itunes.apple.com/us/genre/ios-travel/id6003?mt=8',
               'https://itunes.apple.com/us/genre/ios-utilities/id6002?mt=8',
               'https://itunes.apple.com/us/genre/ios-weather/id6001?mt=8'
            ]

    #indexes=indexes()
    def parse(self, response):#//*[@id="selectedcontent"]/div[2]/ul/li[1]
        for sel in response.xpath('//div[@id="selectedcontent"]/div[1]/ul/li'):
            #/html/body/div[2]/div/table/tr'):#//*[@id="selectedcontent"]/div[1]/ul/li[1]/a
            app = sel.xpath('a')
            link=app.xpath('@href').extract()[0]
            print app
            yield scrapy.Request(link,callback=self.parse_dir_contents)


        for sel in response.xpath('//div[@id="selectedcontent"]/div[2]/ul/li'):
            # /html/body/div[2]/div/table/tr'):#//*[@id="selectedcontent"]/div[1]/ul/li[1]/a
            app = sel.xpath('a')
            link = app.xpath('@href').extract()[0]
            print app
            yield scrapy.Request(link, callback=self.parse_dir_contents)

        for sel in response.xpath('//div[@id="selectedcontent"]/div[3]/ul/li'):
            # /html/body/div[2]/div/table/tr'):#//*[@id="selectedcontent"]/div[1]/ul/li[1]/a
            app = sel.xpath('a')
            link = app.xpath('@href').extract()[0]
            print app
            yield scrapy.Request(link, callback=self.parse_dir_contents)



    def parse_dir_contents(self,response):
        #title://div[@id="title"]/div[1]/h1
        #link://*[@id="left-stack"]/div[1]/a[1]
        #img://div[@id="left-stack"]/div[1]/a[1]/div/img
        #// meta[ @ itemprop = 'image'] / @content
        #description://*[@id="content"]/div/div[2]/div[1]/p
        #recommend://div[@class="swoosh lockup-container application large"]/div[2]/div[1-5]/div[@class="lockup-info"]/ul/li[1]/a/span/text()
        item = StackItem()
        title=response.xpath('//div[@id="title"]/div[1]/h1/text()').extract()[0]
        link=response.xpath('//div[@id="left-stack"]/div[1]/a[1]/@href').extract()[0]
        imgpath=response.xpath("//meta[@itemprop='image']/@content").extract()[0]#response.xpath('//div[@id="left-stack"]/div[1]/a[1]/div/img/@src').extract()[0]
        description=response.xpath('//div[@id="content"]/div/div[2]/div[1]/p/text()').extract()[0]
        recommend=list()
        for sel in response.xpath('//div[@class="swoosh lockup-container application large"]/div[2]/div'):
            rec=sel.xpath('//div[@class="lockup small application"]/@adam-id').extract()#sel.xpath('//div[@class="lockup-info"]/ul/li[1]/a/span/text()').extract()#response.xpath("//div[@class='content']//div[@class='lockup small application']/@adam-id").extract()
            recommend.append(rec)
        item['title']=title
        item['link']=link
        strlist=link.split("/")
        item['id']=strlist[strlist.__len__()-1].split("?")[0][2:]
        item['img']=imgpath#//*[@id="left-stack"]/div[1]/a[1]/div/img
        item['description']=description
        item['recommend']=recommend[0]
        yield item

