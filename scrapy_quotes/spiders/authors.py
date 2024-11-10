import scrapy

from scrapy_quotes.items import AuthorItem


class AuthorSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    custom_settings = {
        'FEEDS': {
            'authors.json': {
                'format': 'json',
                'fields': ['name', 'born_date', 'born_location'],
                'overwrite': True
            },

        },
    }

    def parse(self, response):
        all_authors = response.css('a[href^="/author/"]')
        for author_link in all_authors:
            yield response.follow(author_link, callback=self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_author(self, response):
        data = {
            'name': response.css('h3::text').get(),
            'born_date': response.css('span.author-born-date::text').get(),
            'born_location':
            response.css('span.author-born-location::text').get()
        }
        yield AuthorItem(data)
