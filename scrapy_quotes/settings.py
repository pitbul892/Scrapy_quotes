BOT_NAME = "scrapy_quotes"

SPIDER_MODULES = ["scrapy_quotes.spiders"]
NEWSPIDER_MODULE = "scrapy_quotes.spiders"

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
