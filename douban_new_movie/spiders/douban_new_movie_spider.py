import scrapy


class DoubanNewMovieSpider(scrapy.Spider):
    name = "douban_new_movie_spider"

    allowed_domains = ["http://atjason.com"]

    start_urls = [
        'http://atjason.com',
    ]

    def parse(self, response):
        # yield scrapy.Request(response, callback=self.parse)
        sel = scrapy.Selector(response)
        # sel = scrapy.Selector(response,callback=self.parse)

        # title=sel.xpath("//div[@class='wrapper']/div[@class='content']/div[@class='clearfix']/div[@class='indent']/div/table/tbody/tr[@class='item']/td[@valign='top']/div[@class='pl2']/a/text()").extract()
        title = sel.xpath("//*[@id='posts']/article/header/h1/a/text()").extract()
        time = sel.xpath("//*[@id='posts']/article/header/div/span[1]/time").extract()
        content = sel.xpath("//*[@id='posts']/article/div[1]/p/text()").extract()

        item = {}

        item['title'] = [n.encode('utf-8') for n in title]
        item['content'] = [n for n in content]
        item['time'] = [n for n in time]

        yield item

        print(title,'\n', content,'\n', time)
