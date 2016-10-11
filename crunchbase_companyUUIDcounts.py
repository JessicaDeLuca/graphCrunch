
# count copmanies associated with unique uuid
SELECT uuid, count(company)
FROM holddups
GROUP BY uuid
HAVING count(company) > 1;
