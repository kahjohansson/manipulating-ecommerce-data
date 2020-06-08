import scrapy

class ProductsSpider(scrapy.Spider):
    name = 'products-spider'
    start_urls = [
        'https://www.americanas.com.br/busca/microondas'
    ]

    def parse(self, response):
        for product in response.css(".hFbhrr"):
            title = product.css(".gYIWNc::text").extract_first()
            price = product.css(".dHyYVS::text").extract()[1]

            yield {
                'title': title,
                'price': price
            }

            next_page_url = response.css(".active+ li a::attr(href)").extract_first()
            if next_page_url is not None:
                yield scrapy.Request(response.urljoin(next_page_url))