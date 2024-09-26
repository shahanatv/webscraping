from typing import Any
import scrapy
from scrapy.http import Response


class StoreSpider(scrapy.Spider):
    name = 'store'
    start_urls = ['https://www.mytheresa.com/int_en/men/shoes.html']

    

    def parse(self, response):
        for products in response.css('div.item'):
                
            
            
            yield {
                    'breadcrumbs' :products.css('div.breadcrumb__item::text').get() ,
                    'name' :products.css('div.item__info__header__designer::text').get() ,
                    'brand' :products.css('div.product__area__branding__designer__link::text').get() ,
                    'description' :products.css('a.item__info__name::text').get() ,
                    'price' :products.css('span.pricing__prices__price::text').get() ,
                    'link' :products.css('a.item__link').attrib['href'] ,
                }
            
        next_page = response.css('a.button.button--active').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)    
            