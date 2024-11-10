import scrapy
from scrapy_quotes.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/',]

    custom_settings = {
        'FEEDS': {
            'quotes_text.json': {
                'format': 'json',
                'fields': ['text', 'tags'],
                'overwrite': True
            },
            'quotes_author.json': {
                'format': 'json',
                'fields': ['author'],
                'overwrite': True
        },
}
    }
    def parse(self, response):
        for quote in response.css('div.quote'):
            data = {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('a.tag::text').getall(),
            }
            yield QuoteItem(data)
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse) 

