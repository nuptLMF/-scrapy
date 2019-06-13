# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Userinfo_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()  #用户的ID
    nick_name = scrapy.Field() #昵称
    marital = scrapy.Field()  #婚姻状况
    sign = scrapy.Field()  #星座
    job = scrapy.Field()  #职业
    hometown = scrapy.Field()  # 故乡
    fans_num = scrapy.Field()  #粉丝数
    jokes_num = scrapy.Field()  #糗事数量
    follows_num = scrapy.Field()  #关注数
    comments = scrapy.Field()  #得到的评论的数量
    votes = scrapy.Field()  #笑脸数
    age = scrapy.Field()  #加入糗百的年龄
