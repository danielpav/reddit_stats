# db reddit; table posts; id:integer, submitter:text, subreddit:text, title:text, unix_time:double precision, upvotes:integer

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL
from sqlalchemy import create_engine

# Create an engine instance

alchemyEngine   = create_engine('postgresql+psycopg2://<db_user>:<db_password>@127.0.0.1:5432/<db_name>', pool_recycle=3600);

# Connect to PostgreSQL server

dbConnection    = alchemyEngine.connect();

query = "SELECT * FROM posts;"

# Step 1: Load the CSV data into a pandas DataFrame
data = pd.read_sql(query, alchemyEngine)

# Step 2: Convert the submission times to datetime objects and set it as the index
data['submission_time'] = pd.to_datetime(data['unix_time'], unit='s')
data.set_index('submission_time', inplace=True)

# Additional Step: Sort the data chronologically
data = data.sort_index()
print(data.iloc[0])

# Step 3: Perform time series decomposition
period = 24  # Manually specify the period (24 for daily pattern)
decomposition = STL(data['upvotes'], period=period).fit()

# Rest of the code remains the same...


# Step 4: Obtain the seasonality component
seasonality = decomposition.seasonal

# Step 5: Smooth out the trend component using moving average
trend = decomposition.trend.rolling(window=7, center=True).mean()

# Step 6: Analyze the seasonality component to identify patterns
hourly_avg = seasonality.groupby(seasonality.index.hour).mean()

# Step 7: Conduct statistical analysis (e.g., t-tests or ANOVA) if required
# ... perform statistical tests as needed ...

# Step 8: Visualize the results
plt.figure(figsize=(10, 6))
plt.plot(hourly_avg.index, hourly_avg.values, marker='o')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Upvotes')
plt.title('Fdf Average Upvotes by Hour of the Day')
plt.grid(True)

# Save the figure as a PNG file
plt.savefig('average_upvotes_seasonality_all_year.png')

# Close the plot to avoid the warning message
plt.close()