# -*- coding: utf-8 -*-
import scrapy
from getkonjunctions import colors


class WortbuchSpider(scrapy.Spider):
    name = 'wortbuch'

    # Countries test
    # allowed_domains = ['www.worldometers.info/'] # Never include the http or https protocol here
    # start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    allowed_domains = ['wortwuchs.net/']  # Should not have protocol
    start_urls = ['https://wortwuchs.net/grammatik/konjunktion/liste/']

    def parse(self, response):

        # rows = response.xpath('//strong/text()').extract()

        rows = response.xpath('//tr')

        # print "The rows are"
        # print(colors.HEADER + rows)
        length = len(rows)
        print('*** The length of the rows is *** ', length)

        for row in rows:
            if row.xpath('./td'):
                columns = row.xpath('./td')

                if len(columns) == 3:
                    print('*****')
                    print()
                    print()
                    print('*****')
                    word = columns[0].xpath('./strong/text()').extract_first()
                    text = columns[1].xpath('./text()').extract()
                    text = word.join(text);

                    yield {
                        'word': word,
                        'example': text,
                        'also': columns[2].xpath('./text()').extract_first(),
                    }

        # rows = response.Xpath("//table//tbody//tr")
        # yield {
        #     rows: rows
        # }
