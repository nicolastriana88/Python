import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blog_spider'
    start_urls = ['https://citytv.eltiempo.com/']

    def parse(self, response):
        # Extraer los títulos de los artículos
        for articulo in response.css('article'):
            yield {
                'titulo': articulo.css('h2 a::text').get(),
                'link': articulo.css('h2 a::attr(href)').get(),
            }

        # Seguir el enlace a la siguiente página
        siguiente_pagina = response.css('a.next::attr(href)').get()
        if siguiente_pagina:
            yield response.follow(siguiente_pagina, self.parse)
