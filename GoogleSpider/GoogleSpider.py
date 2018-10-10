# -*- coding: utf-8 -*-
from w3lib.html import remove_tags
import scrapy
import re
import json


class GooglespiderSpider(scrapy.Spider):
    name = 'GoogleSpider'
    allowed_domains = ['www.google.com']
    start_urls = ['https://www.google.com/search?q=intagram gamers "gmail.com"&ei=K2u7W9CkIuvBgAbRhr_wBw&start=0&sa=N&biw=1366&bih=657']
    count = 1

    def parse(self, response):

    	text = remove_tags(str(response.css('span.st').extract()).replace('\\n',''))
    	match = re.findall(r'[\w\.-]+@[\w\.-]+', text)

    	emails = {}

    	for e in match:
    		emails[ 'email-{}'.format(self.count) ] = e
    		self.count = self.count + 1


    	yield emails

    	next_page = response.css('table tr td a.fl::attr(href)').extract()[int(response.css('table#nav b::text').extract_first())]
    	next_page = response.urljoin(next_page)
    	
    	if next_page:
    		yield scrapy.Request(url = next_page, callback = self.parse)
    	
