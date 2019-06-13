# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import Userinfo_Item
import re

class QiushibaikeSpider(scrapy.Spider):
	name = 'qiushibaike'
	allowed_domains = ['www.qiushibaike.com']
	start_urls = 'http://www.qiushibaike.com/users/'
	start_id = ['38269978']
	count = 0
	def start_requests(self):
		url  = '{urls}{keyword}/followers'.format(urls = self.start_urls,keyword = self.start_id[0])
		yield scrapy.Request(url,callback=self.parse_informations)


	def parse_informations(self, response):
		try:
			informations = Userinfo_Item()
			other_ids =';'.join(response.xpath("//div[contains(@class,'col-right')]/div/ul/li/a[1]/@href").extract()) #关注的用户id
			ID_Data = re.findall('users/(\d+)/',other_ids)
			informations['_id'] = re.findall('users/(\d+)',response.url)[0]
			text_ = ';'.join(response.xpath("//div[contains(@class, '-left')]//text()").extract()).replace('\n','').replace(':','')
			informations['marital'] = re.findall('婚姻;(.*?);',text_)[0]  #婚姻状况
			informations['nick_name'] = ''.join(response.xpath("//div[contains(@class,'-cover')]/h2/text()").extract()).replace('\n','')
			informations['sign'] = re.findall('星座;(.*?);',text_)[0]  #星座
			informations['job'] = re.findall('职业;(.*?);',text_)[0]  #职业
			informations['hometown'] = re.findall('故乡;(.*?);',text_)[0]  # 故乡
			informations['fans_num'] = re.findall('粉丝数;(\d+)',text_)[0]  #粉丝数
			informations['follows_num'] = re.findall('关注数;(\d+)',text_)[0] #关注数
			informations['jokes_num'] = re.findall('糗事;(\d+)',text_)[0]  #糗事数量
			informations['comments'] = re.findall('评论;(\d+)',text_)[0]   #得到的评论的数量
			informations['votes'] = re.findall('笑脸;(\d+)',text_)[0]  #笑脸数
			informations['age'] = re.findall('糗龄;(\d+)',text_)[0]+'天'  #加入糗百的年龄
			yield informations

			if ID_Data:    #从用户的粉丝及关注者，用深度遍历提取所有的糗百用户信息
				for ID in ID_Data:
					Relationship_url = 'https://www.qiushibaike.com/users/{}/followers/'.format(ID)
					yield scrapy.Request(url=Relationship_url,meta={'dont_redirect': True,'handle_httpstatus_list': [302]},callback=self.parse_informations) #设置meta拒绝网页跳转
		except:
			pass