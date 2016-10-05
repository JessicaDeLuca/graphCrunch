import os
from pycrunchbase import CrunchBase
import psycopg2
import sys

# when you store a key in your bash_profile it automatically loads to memory
# everytime you open your bash shell so you can call local variables from it

API_KEY = os.environ["crunchbaseapi_ACCESS_KEY_ID"]
cb = CrunchBase(API_KEY)

con = psycopg2.connect("dbname='crunchbase_news' user='jessicadeluca'")

company_names = ['netflix','facebook','linkedin']
#company_names = ['netflix']#,'facebook','linkedin')
#company_names = ['facebook','linkedin']

scrape_companies(company_names)


# pick company name from the list and run scrape company_method
def scrape_companies(company_names):
        for company_name in company_names:
            scrape_company(company_name)

# first page of news is a relationship type but all others are considered pages
# find the company you want, make sure there are sufficient total urls to consider the company
# store first page of news as a variable
# store total count of news for company as a variable
# scrape the first page (references the scrape page code)
# enter for loop for second page until the last page
# turn the page
# scrape the page
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

# scrape the individual page for a given company news items and create a list
    # In [50]: facebook.news
    # Out[50]: news Total: 216482 https://api.crunchbase.com/v/3/organizations/facebook/news

# since the company_name is not page of the page code we are scraping we must
# pass it in as varaible (since it was previously defined), so it is included
# as an entry in our all_news list
def scrape_page(company_name, company_news):
    all_news = []
    for news in company_news:
        all_news.append({'title': news.title, 'company': company_name, 'news_url': news.url, 'uuid': news.uuid,
         'author':news.author, 'posted_on': news.posted_on,
         'created_at': news.created_at, 'updated_at': news.updated_at})

    # At the end of a page (100 entries), write those rows to previously created
    # SQL table
    # need to define variables to add to table as well as the values (in this case
    # all values are strings)

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
# grab book, open book vs turn pages of the book (need first page called
# differently than all subsequent pages)
