# db reddit; table posts; id:integer, submitter:text, subreddit:text, title:text, unix_time:double precision, upvotes:integer

import psycopg2
import csv

conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="db_name",
    user="db_user",
    password="db_password"
)

conn.autocommit = True
cursor = conn.cursor()


sql = '''COPY posts(submitter, subreddit, title, unix_time, upvotes)
FROM '/path/to/reddit_statistics/Data/posts.csv'
DELIMITER ','
CSV HEADER;'''

cursor.execute(sql)

conn.commit()
conn.close()