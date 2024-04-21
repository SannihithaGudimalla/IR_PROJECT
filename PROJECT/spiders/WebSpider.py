import scrapy
from PROJECT.settings import CUSTOM_SETTINGS

class WebspiderSpider(scrapy.Spider):
    # Initializing the web crawler
    name = "WebSpider"
   
    #initializing seed urls
    start_urls = ['https://www.splashlearn.com/blog/friendship-quotes-for-kids/',
                  'https://www.amazon.com/',                  
                  'https://en.wikipedia.org/wiki/Lion',
                  'https://www.goodreads.com/quotes/tag/life-experience',
                  'https://www.rei.com/c/backpacks',
                  'https://www.patagonia.com/shop/luggage-travel-duffel-bags',
                  'https://www.randomactsofkindness.org/kindness-quotes',
                  'https://www.jewelosco.com/',
                  'https://www.ashleyfurniture.com/c/furniture/living-room/sofas/reclining-sofas/']
    
    # importing custom settings from settings.py file
    custom_settings = CUSTOM_SETTINGS

    def parse(self, response):
        yield {
            'url': response.url,
            'title': response.css('title::text').get(),
            'content': response.css('body').get(),
        }
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)
