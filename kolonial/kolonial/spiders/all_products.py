# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider
from scrapy.exceptions import IgnoreRequest

from ..items import ProductItem


class AllProductsSpider(SitemapSpider):
    name = "get_all_products"
    allowed_domains = ["kolonial.no"]
    sitemap_urls = ["http://www.kolonial.no/sitemap.xml"]

    # ("/produkter/15543", "parse_product"),
    # ("/produkter/27730", "parse_product"),
    # ("/produkter/15933", "parse_product"),
    # ("/produkter/28754", "parse_product"),

    sitemap_rules = [
        ("/produkter/", "parse_product"),
    ]

    # Can take input like id or different urls etc.
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def sitemap_filter(self, entries):
    #     for entry in entries:
    #         date_time = datetime.strptime(entry['lastmod'], '%Y-%m-%d')
    #         if <expression>:
    #             yield entry

    def parse_product(self, response):
        meta_info = dict(
            (meta.attrib.get("property"), meta.attrib.get("content"))
            for meta in response.css("meta")
            if (meta.attrib.get("property") and meta.attrib.get("content"))
        )

        if meta_info:
            yield {
                "title": meta_info.get("og:title"),
                "price": meta_info.get("product:price:amount"),
                "url": meta_info.get("og:url"),
                "image": meta_info.get("og:image"),
                "currency": meta_info.get("product:price:currency"),
                "description": meta_info.get("og:description"),
            }
