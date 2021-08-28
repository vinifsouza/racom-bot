import os
import sys

from scrapy.crawler import CrawlerProcess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scrap.scrap.spiders.faq_spider import FaqSpider

def start_scrap():
    process = CrawlerProcess(settings = {
        'LOG_ENABLED': False
    })

    process.crawl(FaqSpider)
    process.start()