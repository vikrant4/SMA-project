import sys
import json
import pandas as pd

def main():
  fileName = sys.argv[1]
  outFileName = sys.argv[2]
  twitterUserNames(fileName, outFileName)

def twitterUserNames(fileName, outFileName):
  userNames = []
  with open(fileName, 'r') as r:
    for line in r:
      if len(line) <= 2:
        continue
      tweet = json.loads(line)
      tweetUser = tweet.get('user', '')['scrren_name']
      tweetRetweet = tweet.get('retweet_count', '')
      tweetFavourite = tweet.get('favourite_count', '')
      userNames.append([tweetUser, tweetRetweet, tweetFavourite])
  return pd.DataFrame(data=userNames, columns=['user_name', 'retweet', 'favourite'])

if __name__ == '__main__':
  main()