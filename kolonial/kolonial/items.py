# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    title: str = scrapy.Field()
    description: str = scrapy.Field()
    price: float = scrapy.Field()
    image: str = scrapy.Field()
    url: str = scrapy.Field()
    currency: str = scrapy.Field()
