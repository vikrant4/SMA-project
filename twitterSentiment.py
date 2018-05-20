import json
import nltk
import string
import pandas as pd
from tweetProcess import TweetProcess
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
import sys

def main():
  sentimentAnalysis(sys.argv[1], sys.argv[2], sys.argv[3])


def sentimentAnalysis(fileName, city, outFileName):
  """
  Perform Vader sentiment analysis on tweet data and filters out negative sentiment tweets with their id and file index
  to outFile.
  Usage: sentimentAnalysis([infile].json, [city], [outfile].csv)
  """
  tweetTokenizer = TweetTokenizer()
  punct = list(string.punctuation)
  stopwordList = stopwords.words('english') + punct + ['rt', 'via', '...']
  vaderSent = vaderSentimentAnalysis(fileName, tweetTokenizer, stopwordList)
  vaderSent['city'] = city
  vaderSent = vaderSent[vaderSent['sentiment'] < 0]
  vaderSent.to_csv(outFileName)

def vaderSentimentAnalysis(fileName, tokenizer, stopWords):
  sentAnalyser = SentimentIntensityAnalyzer()
  tSentiment = []

  with open(fileName, 'r') as r:
    for line in r:
      if len(line) <= 2:
        continue
      tweet = json.loads(line)

      try:
        tweetText = tweet.get('text', '')
        tweetID = tweet.get('id', '')

        lTokens = TweetProcess(tweetText, tokenizer, stopWords, 'all')
        sentimentScore = sentAnalyser.polarity_scores(" ".join(lTokens))
        tSentiment.append([tweetID, sentimentScore['compound']])
      except KeyError as e:
        print(e)
  sentimentDF = pd.DataFrame(data=tSentiment, columns=['id', 'sentiment'])
  return sentimentDF


if __name__ == '__main__':
  main()
