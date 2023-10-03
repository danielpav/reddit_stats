import praw
import csv
import pandas as pd
import os

reddit = praw.Reddit(
    client_id='your client id',
    client_secret='your client secret',
    user_agent='your user agent'
)

submitters = []
posts = []

with open('/home/daniel/projects/reddit/Data/top_submitters.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        submitters.append(row[0])

subreddit_names = ["wallstreetbets", "stocks", "investing", "stockmarket", "options", "robinhoodpennystocks",]

for submitter in submitters:
    redditor = reddit.redditor(submitter)
    print(redditor.name)
    try:
        top_posts = redditor.submissions.top()
        for post in top_posts:
                print(post.subreddit)
                if post.subreddit in subreddit_names:
                    print(post.title)
                    title = post.title
                    subreddit = post.subreddit
                    author = submitter
                    timestamp = post.created_utc
                    score = post.score
                    posts.append([submitter, subreddit, title, timestamp, score])
    except:
        continue

df = pd.DataFrame(posts)

df.to_csv("/home/daniel/projects/reddit/Data/posts.csv", sep=',', index=False)
