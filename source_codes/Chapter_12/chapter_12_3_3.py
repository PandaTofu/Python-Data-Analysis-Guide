response.body[0:138]

response.selector

response.xpath('//title/text()')

response.css('title::text')

response.xpath('//title/text()').extract()

response.xpath('//title/text()').re(r':\s*(.*)')

response.xpath('//tr/td/table[@border=1][@cellpadding=5]')

sel_list = response.xpath('//tr/td/table[@border=1][@cellpadding=5]').xpath('tr')[1:]

sel_list[0].xpath('td/*//b/a/text()').extract()

sel_list[0].xpath('td/p/text()').extract()

