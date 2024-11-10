import scrapy


class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class AuthorItem(scrapy.Item):
    name = scrapy.Field()
    born_date = scrapy.Field()
    born_location = scrapy.Field()
