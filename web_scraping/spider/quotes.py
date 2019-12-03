import scrapy

class quotes(scrapy.Spider):
    name = 'quotes'
    star_urls = [
        ''
    ]

    def parse(self, response):
        for quote in response.css('div.quotes'):
            yield {

                'author': quote.css('p.author::text').extract_first(),
                'quote': quote.css('p.aquote::text').extract(),



            }
