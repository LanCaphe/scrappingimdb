import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MoviesSpider(CrawlSpider):
    name = 'movies'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//td[@class="titleColumn"]/a'), callback = 'parse_item', follow = True),
        )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//h1/text()').get()
        item['synopsis'] = response.xpath('//span[contains(@class,"GenresAndPlot__TextContainerBreakpointXL-cum89p-2 gCtawA")]/text()').get()
        item['original title'] = response.xpath('//div[@class="OriginalTitle__OriginalTitleText-jz9bzr-0 llYePj"]/text()').get()
        item['date'] = response.xpath('//span[@class="TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex"]/text()').get()
        item['score'] = response.xpath('//span[@class="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"]/text()').get()
        item['type'] = response.xpath('//div[@data-testid="genres"]//span/text()').getall()
        item['actors'] = response.xpath('//a[@class="StyledComponents__ActorName-y9ygcu-1 eyqFnv"]/text()').getall()
        item['duration'] = response.xpath('//li[@data-testid="title-techspec_runtime"]//div/text()').getall()

      

        return item
