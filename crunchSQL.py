import os
from pycrunchbase import CrunchBase
import psycopg2
import sys

API_KEY = os.environ["crunchbaseapi_ACCESS_KEY_ID"]
cb = CrunchBase(API_KEY)

con = psycopg2.connect("dbname='crunchbase_news' user='jessicadeluca'")

# when you store a key in your bash_profile it automatically loads to memory
# everytime you open your bash shell so you can call local variables from it

# Here: create the postresSQL database with schema as
# * CompanyId: string
# * news_url: string

# build sql database
# github = cb.organization('github')

def scrape_companies(company_names):
        for company_name in company_names:
            scrape_company(company_name)

def scrape_company(company_name):

    print company_name
    company = cb.organization(company_name)
    if company.news.total_items < 10000:
        return
    page = cb.more(company.news)
    number_of_pages = page.number_of_pages
    scrape_page(company.name, page)
    for i in xrange(number_of_pages - 1):
        print "i =", i
        page = cb.more(page)
        scrape_page(company.name, page)

def scrape_page(company_name, company_news):
    all_news = []
    for news in company_news:
        all_news.append({'title': news.title, 'company': company_name, 'news_url': news.url, 'uuid': news.uuid,
         'author':news.author, 'posted_on': news.posted_on,
         'created_at': news.created_at, 'updated_at': news.updated_at})

    #print all_news
    #print len(all_news)

    cur = con.cursor()
    cur.executemany("""
    INSERT INTO cb_news(
        uuid, company, title, news_url, author, posted_on, created_at, updated_at)
    VALUES (
        %(uuid)s, %(company)s, %(title)s, %(news_url)s, %(author)s, %(posted_on)s,
        %(created_at)s, %(updated_at)s)""", all_news)
    con.commit()
#
# all urls for first page and url for next page
# cb.more take company news and go to the next page
# grab book, open book vs turn page



company_names = ['netflix','facebook','linkedin']
#company_names = ['netflix']#,'facebook','linkedin')
#company_names = ['facebook','linkedin']

scrape_companies(company_names)

# #  all_news_urls
# for news in all_news:
#     INSERT (company, title, news_url, uuid, author, posted_on,
# created_at, updated_at) INTO <cb_news>
#     db.insert(company, news_url)
#
#
# CREATE TABLE crunchbase_news (
#     CompanyID            string,
#     CompanyName        string,
#     newa_url
# );




# select all urls with more than one
