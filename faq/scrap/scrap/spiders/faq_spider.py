import json

import scrapy

class FaqSpider(scrapy.Spider):
    name = 'faq'
    start_urls = ['https://mooc.campusvirtual.fiocruz.br/rea/coronavirus/faq.html']

    def parse(self, response):
        pills = []

        for pill in response.css('ul#pills-tab li:not(.nav-item.dropdown) a'):
            try:
                pills.append({
                    'id': pill.attrib['aria-controls'],
                    'name': ''.join(pill.css('::text').getall())
                })
            except:
                pass

        faqs = []

        for pill in pills:
            temp_dict = {
                'id': pill['id'],
                'category': pill['name'],
                'faqs': []
            }

            actual_pill = response.css('div#%s' %pill['id'])

            for _ in actual_pill:

                for li in actual_pill.css('ul > li'):
                    li_href = li.css('a.collapsed::attr(href)').get()

                    if li_href:
                        faq_id = li_href.replace('#', '')

                        question = ''.join(li.css('a::text').getall())
                        question = question[question.find(')')+1:].strip()

                        answer = ''.join(li.css('div#%s' %faq_id).getall())

                        if question and answer:
                            faq = {
                                'question': question,
                                'answer': answer
                            }

                            temp_dict['faqs'].append(faq)

            faqs.append(temp_dict)

        with open('output.json', 'w') as f:
            json.dump(faqs, f)

