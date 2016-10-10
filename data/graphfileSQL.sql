
SELECT company, COUNT(news_url)
FROM cb_news GROUP BY news_url, company
HAVING (COUNT(news_url) > 1 );
