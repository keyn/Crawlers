# -*- coding: utf-8 -*-
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    login_url = "http://quotes.toscrape.com/login"
    start_urls = [login_url]

    def parse(self, response):
        # extract the csrf
        token = response.css('input[type=hidden]::attr(value)').extract_first()
        # create python dict with the form values
        data = {
            'csrf_token': token,
            'username' : 'abc',
            'password' : 'abc',
        }
        #submit a Post request to it
        yield scrapy.FormRequest(url=self.login_url , formdata = data , callback = self.parse_quotes)

    def parse_quotes(self,response):
        for q in response.css('div.quote'):
            yield {
                'author_name' : q.css('small.author::text').extract_first(),
                'author_url' : q.css('small.author ~ a[href*="goodreads.com"]::attr(href)').extract_first(),
            }