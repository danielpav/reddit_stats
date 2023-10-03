import praw
import pandas as pd
import os

reddit = praw.Reddit(
    client_id='your client id',
    client_secret='your client secret',
    user_agent='your user agent'
)

subreddit_name = "wallstreetbets"
subreddit = reddit.subreddit(subreddit_name)

top_posts = subreddit.top(time_filter='all', limit=1000)
submissions = {}

i = 0
for post in top_posts:
    try:
        author = post.author.name
        i = i + 1
        print(i, author)
        if author in submissions:
            submissions[author] += 1
        else:
            submissions[author] = 1
    except:
        continue

top_submitters = sorted(submissions.items(), key=lambda x: x[1], reverse=True)[:200]

# Create Pandas DataFrame
df = pd.DataFrame.from_dict(top_submitters)

df.to_csv(f"/home/daniel/projects/reddit/Data/{subreddit_name}_top_submitters_b.csv", sep=',', index=False)
