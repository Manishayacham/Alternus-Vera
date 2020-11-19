# -*- coding: utf-8 -*-
"""headline_scraper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n4LObRrkLl09yaS-SrBPP0tOQCijWdQf
"""

import scrapy
from pandas import read_csv
from readability.readability import Document

PATH_TO_DATA = 'https://gist.githubusercontent.com/jackbandy/208028b404d8c6a6f822397e306a5a34/raw/ef7f73357e77c29c63b5b7632d840a923327e179/100_urls_sample.csv'


class HeadlineSpider(scrapy.Spider):
    name = "headline_spider"
    start_urls = read_csv(PATH_TO_DATA).url.tolist()

    def parse(self, response):
        doc = Document(response.text)
        yield {
            'short_title': doc.short_title(),
            'full_title': doc.title(),
            'url': response.url
        }