import pandas as pd
from sqlalchemy import create_engine

def get_posts_from_db(subreddit=None):
    # Create an engine instance

    alchemyEngine   = create_engine('postgresql+psycopg2://<db_user>:<db_password>@localhost:5432/<db_name>', pool_recycle=3600);

    # Connect to PostgreSQL server

    dbConnection    = alchemyEngine.connect();
    
    if subreddit:
        query = "SELECT * FROM posts WHERE subreddit = '" + subreddit + "';"
    else:
        query = "SELECT * FROM posts;"

    # Step 1: Load the CSV data into a pandas DataFrame
    data = pd.read_sql(query, alchemyEngine)

    # Step 2: Convert the submission times to datetime objects and set it as the index
    data['submission_time'] = pd.to_datetime(data['unix_time'], unit='s')
    date_format = "%Y-%m-%d %H:%M:%S"
    data['submission_time'] = data['submission_time'].dt.strftime(date_format)

    # Rename the columns
    # data = data.rename(columns={'upvotes': 'y', 'submission_time': 'ds'})
    data = data.rename(columns={'title': 'Title', 'upvotes': 'Score', 'submitter': 'Submitter'})

    # Additional Step: Sort the data chronologically
    data = data.sort_index()
    print(data.iloc[0])

    return data