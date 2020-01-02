import scrapy
import cfscrape


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            # 'http://quotes.toscrape.com/',
            'https://www.directliquidation.com/electronics/?s=&idx=dl_prod_posts_product_end_date_ts_asc&page=10',
        ]
        cf_requests = []
        for url in urls:
            token, agent = cfscrape.get_tokens(url, 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like asdlkjqwdj) Chrome/16.0.912.36 Safari/535.7')
            print("The token is ", token)
            print("The user agent is", agent)
            cf_requests.append(scrapy.Request(url=url, cookies=token, headers={'User-Agent': agent}))
        return cf_requests
            # yield scrapy.Request(url=url, callback=self.parse)  


    # def parse(self, response):
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'text': quote.css('span.text::text').get(),
    #             'author': quote.css('small.author::text').get(),
    #             'tags': quote.css('div.tags a.tag::text').getall(),
    #         }

    #     next_page = response.css('li.next a::attr(href)').get()
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page, callback=self.parse)
            
    def parse(self, response):
        filename = 'quotes.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)