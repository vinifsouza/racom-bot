import os
import sys

from scrapy.crawler import CrawlerProcess


from scrap.scrap.spiders.faq_spider import FaqSpider


def start_scrap():
    process = CrawlerProcess(settings={
        'LOG_ENABLED': False
    })

    process.crawl(FaqSpider)
    process.start()
