import os
from pycrunchbase import CrunchBase

# when you store a key in your bash_profile it automatically loads to memory
# everytime you open your bash shell so you can call local variables from it
API_KEY = os.environ["crunchbaseapi_ACCESS_KEY_ID"]
cb = CrunchBase(API_KEY)
company = cb.organization ('netflix')

all_news = []
def scrape_page(company_news):
    for news in company_news:
        all_news.append({'title': news.title, 'news_url': news.url, 'uuid': news.uuid,
         'author':news.author, 'posted_on': news.posted_on,
         'created_at': news.created_at, 'updated_at': news.updated_at})

# all urls for first page and url for next page
# cb.more take company news and go to the next page
# grab book, open book vs turn page

company_news = company.news
scrape_page(company_news)
for i in xrange(5):
    company_news = cb.more(company_news)
    scrape_page(company_news)
    break


# #  all_news_urls
# for news in all_news:
#     INSERT (company, title, news_url, uuid, author, posted_on,
#        posted_on_trust_code,created_at, updated_at) INTO <crunchbase_news>
#     db.insert(company, news_url)
#
#
# CREATE TABLE crunchbase_news (
#     CompanyID            string,
#     CompanyName        string,
#     newa_url
# );




# select all urls with more than one
