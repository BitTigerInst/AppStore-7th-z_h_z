# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymongo

class AppstorePipeline(object):
	# def __init__(self):
	# 	connection = pymongo.MongoClient()
	# 	db = connection["appStore"]
	# 	self.collection = db["appStore"]
	def process_item(self,item,spider):
		# self.collection.insert(dict(item))
		return item
