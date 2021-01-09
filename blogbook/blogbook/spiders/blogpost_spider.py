import scrapy


class BlogpostSpider(scrapy.Spider):
     name = 'blogposts'

     start_urls = [
         'https://myblogbook.xyz/posts/'
     ]

     def parse(self,response):
         for post in response.css('div.thumbnail'):
            #  print(post.css('.caption h3 a p::text').get())
             yield{
                 'title': post.css('.caption h3 a p::text').get(),
                 'date': post.css('.caption h3 small::text').get(),
                 'author': post.css('.caption p::text').get()
             }
         next_page = response.css('.pagination span a::attr(href)').get()
         if next_page is not None:
             next_page = response.urljoin(next_page)
             yield scrapy.Request(next_page,callback=self.parse)