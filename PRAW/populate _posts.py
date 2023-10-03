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

with open('/home/daniel/projects/reddit/Data/top_submitters_b.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        submitters.append(row[0])

subreddit_names = ["wallstreetbets", "stocks", "investing", "stockmarket", "options", "robinhoodpennystocks", "pennystocks"]

done = 0
while done == 0:
    for submitter in submitters:
        try:
            redditor = redditor.submitter(submitter)
        except:
            submitters.remove(submitter)

for submitter in submitters:
    try:
        redditor = reddit.redditor(submitter)
        print(redditor.name)
        top_posts = redditor.submissions.top()
    except:
        continue

    for post in top_posts:
        try:
            if post.subreddit in subreddit_names:
                title = post.title
                subreddit = post.subreddit
                author = submitter
                timestamp = post.created_utc
                score = post.score
                posts.append([submitter, subreddit, title, timestamp, score])
        except:
            continue

df = pd.DataFrame(posts)

df.to_csv("/home/daniel/projects/reddit/Data/posts_b.csv", sep=',', index=False)