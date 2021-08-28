import os
import sys

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scrap.scrap.spiders.faq_spider import FaqSpider

def start_scrap():
    process = CrawlerProcess(get_project_settings())

    process.crawl(FaqSpider)
    process.start()