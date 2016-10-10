# Find duplicate records and remove them from cb_news

# https://support.microsoft.com/en-us/kb/139444

# Make a copy of cb_news in case something goes wrong?
SELECT *
INTO cb_news_backup
FROM cb_news;

# identify duplicates (not just uuid duplicates but uuid and company duplicates)
SELECT uuid, company, count(*)
FROM cb_news
GROUP BY uuid, company
HAVING count(*) > 1;

# select duplicate key-values into a holding table called 'holdkey'

SELECT uuid, company, count(*)
INTO holdkey
FROM cb_news
GROUP BY uuid, company
HAVING count(*) > 1

# Select the duplicate rows into a holding table, holddups
# (eliminating duplicates in the process)

SELECT DISTINCT cb_news.*
INTO holddups
FROM cb_news, holdkey
WHERE cb_news.uuid = holdkey.uuid
AND cb_news.company = holdkey.company

# Delete the duplicate rows from the original table

DELETE cb_news
FROM cb_news, holdkey
WHERE cb_news.uuid = holdkey.uuid
AND cb_news.company = holdkey.company

# Put the unique rows back into the table

INSERT cb_news SELECT * FROM holddups
