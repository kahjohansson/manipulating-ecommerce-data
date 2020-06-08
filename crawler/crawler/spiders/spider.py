import scrapy
from ..items import ProductItem

class ProductsSpider(scrapy.Spider):
    name = 'products-spider'
    start_urls = [
        'https://www.americanas.com.br/busca/microondas'
    ]

    def parse(self, response):

        c_product = ProductItem()

        for product in response.css(".hFbhrr"):
            title = product.css(".gYIWNc::text").extract_first()
            price = product.css(".dHyYVS::text").extract()[1]

            c_product['title'] = title
            c_product['price'] = price

            yield c_product

            next_page_url = response.css(".active+ li a::attr(href)").extract_first()
            if next_page_url is not None:
                yield scrapy.Request(response.urljoin(next_page_url))