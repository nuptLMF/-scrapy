# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from qsbk.settings import MONGO_URI,MONGO_PORT,DB_NAME
from qsbk.items import Userinfo_Item
class QsbkPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoDBPipeline(object):
	def __init__(self):
		DATA = pymongo.MongoClient(MONGO_URI,MONGO_PORT)
		db = DATA[DB_NAME]
		self.Information = db["Informations"]

	def process_item(self,item,spider):
		self.Information.update_one({'_id':item['_id']},{'$set':item},True)  #用跟新的方法存储糗百用户的个人信息达到入库去重效果
		return item 

