# SMA-project

## Data collection
Data is first collected using the REST API to target the tweets of past 7 days from major metropolitan cities of Australia. Tweets from each city is stored in files named [city].json. After tweets from REST API were collected to maximum extent, the streaming API is used to target all tweets being generated within Australia and targets only those which include any of the query parameters. The script for streaming data is in twitterStreaming.py.

Run the following command to collect data from streaming API. You can use other keywords to target tweets.

`python .\twitterStreaming.py streamAus.json gov government tax taxes budget federal ethics ethical sustainable`
