import scrapy
import db_processor

def processor_articles(articles):
    for article in articles:
        db_processor.insert_into_articles(article)

class SkkuSpiderSpider(scrapy.Spider):
    name = "skku_spider"
    allowed_domains = ["forensic.skku.edu"]
    start_urls = ["https://forensic.skku.edu/forensic/community/grad_notice.do"]

    def parse(self, response):
        articles = []
        for article in response.css("ul.board-list-wrap > li"):
            data = {
                "title": article.css("dl > dt a::text").get().replace("\n", "").replace("\t", "").replace(" ", ""), #text는 모두 가지고 있는 요소라 attr() 불필요             "link": article.css("dl > dt a::attr(href)").get() #href는 a만 가지고 있는 속성이라 attr() 붙여줘야함
                "link" : article.css('dl > dt a::attr(href)').get()
            }
            articles.append(data)
        print(articles)
        processor_articles(articles)

            # Copy -> Copy selector
            # Copy selector 예시: jwxe_main_content > div > div > div.board-name-list.board-wrap > ul > li:nth-child(1) > dl

        # for page in response.css("ul.paging-wrap li"): #다음페이지로 넘어갈 수 있게 하는 함수
        #     link = page.css('a::attr(href)').get()
        #     link_text = page.css('a::text').get()

        #     if link_text:
        #         link_text = link_text.strip() #strip(): 공백을 없애라

        #     if link_text and link_text.isdigit() and int(link_text) <= 3: #isdigit(): 숫자고 null아니고
        #         yield{'page_number': link_text, 'link': link}
        #         yield response.follow(link, self.parse) #self: 한 번 더 실행해라

