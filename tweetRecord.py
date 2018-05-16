import sys
from twitterClient import twitterClient
from tweepy import Cursor
import json

def main():
  """
  Usage: tweetRecord.py <out filename> <location> <list of query terms>
  Example: For collecting tweets from Melboune you may run
    python .\\tweetRecord.py data.json melbourne government gov
  It is our choice to keep all the data in same file or create seperate
  files for each location
  """
  assert(len(sys.argv) > 3)
  outFileName = sys.argv[1]
  location = sys.argv[2]
  query = " ".join(sys.argv[3:])

  locationParser = {
    'melbourne': "-37.814735,144.967691,40km",
    'sydney': "-33.868619,151.207889,40km",
    'brisbane': "-27.465590,153.026827,40km",
    'perth': "31.947990,115.862838,40km",
    'darwin': "-12.429747,130.850908,40km",
    'adelaide': "-34.925426,138.599653,40km",
    'canberra': "-35.279413,149.128835,40km",
    'goldcost': "-28.003662,153.405029,40km",
    'newcastle': "-32.937118,151.702394,40km"
  }

  client = twitterClient()
  count = 0
  lastTweet = {}
  try:
    with open(outFileName, 'a') as f:
      for tweet in Cursor(client.search, q=query, geocode=locationParser[location]).items(1500):
        print('tweet no: ', count)
        count+=1
        f.write("{}\n".format(json.dumps(tweet._json)))
        lastTweet = tweet
  except Exception as e:
    print(e)
  finally:
    print(lastTweet)


if __name__ == '__main__':
  main()
