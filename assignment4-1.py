import psycopg2
import pandas as pd

# Connection parameters
conn = psycopg2.connect(
    host="code001.ecsbdp.com",
    port=5432,
    database="chinook",
    user="larry",
    password="iddqd"
)

# set query to calculate the average total sales for customers who have bought Jazz tracks vs those who haven't
query = """
WITH customer_totals AS (
    SELECT 
        c.customer_id,
        SUM(i.total) AS total_sales
    FROM customer c
    JOIN invoice i ON c.customer_id = i.customer_id
    GROUP BY c.customer_id
),
jazz_customers AS (
    SELECT DISTINCT c.customer_id
    FROM customer c
    JOIN invoice i ON c.customer_id = i.customer_id
    JOIN invoice_line il ON i.invoice_id = il.invoice_id
    JOIN track t ON il.track_id = t.track_id
    JOIN genre g ON t.genre_id = g.genre_id
    WHERE g.name = 'Jazz'
)
SELECT 
    CASE 
        WHEN ct.customer_id IN (SELECT customer_id FROM jazz_customers)
        THEN 'Jazz Buyers'
        ELSE 'Non-Jazz Buyers'
    END AS customer_type,
    AVG(ct.total_sales) AS avg_total_sales
FROM customer_totals ct
GROUP BY customer_type;
"""

# Execute and load into DataFrame
df = pd.read_sql(query, conn)

# Close connection
conn.close()

print(df)
df.to_csv("results4-1.csv", index=False)