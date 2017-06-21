"""
From scrapy tutorial: https://doc.scrapy.org/en/latest/intro/tutorial.html

STEPS:
    Start project: scrapy startproject [projectname]
    Create first spider: lives in [projectname]/spiders directory
        Name it: quotes_spider.py
        Fill it with some code (example):
            """
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "spider1"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract()
            }
            """

    Go to main directory(scraped/extracted files will be saved there), test run the spider: scrapy crawl quotes (this will run the spider called "quotes" as defined in the quotes_spider.py file)
    Run the spider again but save data:
        Example: scrapy crawl quotes -o quotes.csv

    Practice commands to extract data using the scrappy shell:
        scrapy shell 'http://quotes.toscrape.com/page/1/'

"""
