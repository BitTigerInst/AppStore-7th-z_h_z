# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppstoreItem(scrapy.Item):
    # define the fields for your item here like:
    appID = scrapy.Field()
    name = scrapy.Field()
    category = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    rating = scrapy.Field()
    related_app = scrapy.Field()
    iPhone_screenShot = scrapy.Field()
    iPad_screenShot = scrapy.Field()
    lauch_time = scrapy.Field()
    current_reviewCount = scrapy.Field()
    all_reviewCount = scrapy.Field()
