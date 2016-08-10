# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PopularappstoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    appID = scrapy.Field()
    name = scrapy.Field()
    category = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    aggregateRating = scrapy.Field()
    related_app = scrapy.Field()
    iPhone_screenShot = scrapy.Field()
    iPad_screenShot = scrapy.Field()
    lauch_time = scrapy.Field()
    currentRating = scrapy.Field()
    # current_ratingValue = scrapy.Field()
    allRating = scrapy.Field()
    # all_ratingValue = scrapy.Field()
