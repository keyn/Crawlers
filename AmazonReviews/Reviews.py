# -*- coding: utf-8 -*-
import scrapy


class ReviewsSpider(scrapy.Spider):
    name = 'Reviews'
    allowed_domains = ['amazon.fr']
    start_urls = ["https://www.amazon.fr/Amazon-génération-Enceinte-connectée-anthracite/product-reviews/B079PNT5TK/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&reviewerType=all_reviews&pageNumber={}&filterByStar=critical".format(i) for i in range(1,40)]

    def parse(self, response):
        reviews = response.css('div[id^=customer_review]')

        for rev in reviews:
            r = {
                'review_author' : rev.css('span[data-hook="review-author"] > a::text').extract_first(),
                'review_date' : rev.css('span[data-hook="review-date"]::text').extract_first(),
                'review_title' :rev.css('a[data-hook="review-title"]::text').extract_first(),
                'review_supporters': rev.css('span[data-hook="helpful-vote-statement"]::text').extract_first()
            }
            yield r
