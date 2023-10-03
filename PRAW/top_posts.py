import praw
import pandas as pd
import datetime as dt

# Authenticate with Reddit API
reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent')

# Set subreddit name
subreddit_name = 'wallstreetbets'

# Get subreddit instance
subreddit = reddit.subreddit(subreddit_name)

# Get top 10000 posts from the past year
top_posts = subreddit.top(time_filter='year', limit=1000)

# Initialize lists to store post data
titles = []
timestamps = []
upvotes = []

# Loop through each post and extract relevant data
for post in top_posts:
    titles.append(post.title)
    timestamps.append(dt.datetime.fromtimestamp(post.created_utc))
    upvotes.append(post.score)

# Create Pandas DataFrame
df = pd.DataFrame({'submission_time': timestamps, 'upvotes': upvotes})

# Print the first 5 rows of the DataFrame
# print(df)

df.to_csv('Fdf_year.csv', sep=',', index=False, header=["submission_time", "upvotes"])
