import os
import json
from time import sleep

from helpers import get_file_name

from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher

from kolonial.spiders.all_products import AllProductsSpider


def get_products():
    filename = "results/" + get_file_name()
    if not os.path.isfile(filename):
        fetch_products()
    with open(filename) as json_file:
        return json.load(json_file)
    return []


def spider_result():
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess(get_project_settings())
    process.crawl(AllProductsSpider)
    process.start()

    with open("results/" + get_file_name(), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)


def fetch_products():
    print("\n > Jeg har desverre ikke hentet dagens produkter :(")
    sleep(0.5)
    print("\n > Jeg jobber med å finne dagens produkter for deg...")
    sleep(0.5)
    print("\n > Syng gjerne en sang mens du venter :)")
    spider_result()
