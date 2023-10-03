import praw
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

reddit = praw.Reddit(
    client_id='your client id',
    client_secret='your client secret',
    user_agent='your user agent'
)

#add username
username = ''
redditor = reddit.redditor('username')

posts = redditor.submissions.top(time_filter="all")
comments = redditor.comments.top(limit=1000)
submissions = {}

for post in posts:
     time = post.created_utc
     print(dt.datetime.fromtimestamp(time))

comments_utc = []
comment_times = []

for comment in comments:
    comment_date = comment.created_utc
    
    comment_time = dt.datetime.fromtimestamp(comment_date).hour
    comments_utc.append(comment_date)
    comment_times.append(comment_time)
    print(dt.datetime.fromtimestamp(comment_date))
    print(comment_time)

# data = pd.DataFrame()

# plt.scatter(comments_utc, comment_times)
# plt.show()
# plt.savefig("comment_graph.png")