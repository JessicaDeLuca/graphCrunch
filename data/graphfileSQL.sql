

SELECT company, news_url, COUNT(news_url)
FROM cb_news GROUP BY news_url, company
HAVING (COUNT(news_url) > 1 );


" Get list of common articles for 2 companies"
   SELECT a.company, b.company, a.title, a.uuid, a.news_url, a.posted_on
   FROM holddups as a
   INNER JOIN holddups as b
   ON a.uuid=b.uuid
  WHERE a.company='Netflix' AND b.company = 'Google'

"Count of edges for each pair of companies"
  SELECT a.company, b.company, count(a.uuid)
  FROM holddups as a
  INNER JOIN holddups as b
  ON a.uuid=b.uuid
  GROUP BY a.company, b.company
  HAVING a.company='Netflix' AND b.company = 'Google'

  SELECT a.company, b.company, count(a.uuid) FROM holddups as a INNER JOIN holddups as b ON a.uuid=b.uuid GROUP BY a.company, b.company LIMIT 10

  
