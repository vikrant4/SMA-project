import json
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import string
import sys

from tweetProcess import TweetProcess

from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pyLDAvis.sklearn


def main():
    topicModelling(sys.argv[1], sys.argv[2], sys.argv[3])


def topicModelling(sentimentIdFile, tweetFile, outFileName):

    tweetTokenizer = TweetTokenizer()
    punct = list(string.punctuation)
    stopwordList = stopwords.words('english') + punct + ['rt', 'via', '...']
    tweetSentiment = {'index':[0]}

    lTweets = []
    if sentimentIdFile != 'null':
        tweetSentiment = pd.read_csv(sentimentIdFile, index_col=0)

    with open(tweetFile, 'r') as r:
        for fIndex, line in enumerate(r):
            if len(line) <= 2:
                continue
            elif sentimentIdFile is not 'null' and fIndex in tweetSentiment.index:
                tweet = json.loads(line)
                tweetText = tweet.get('text', '')

                tokens = TweetProcess(
                    tweetText, tweetTokenizer, stopwordList, 'all')
                lTweets.append(" ".join(tokens))

    no_features = 1500

    tfVectorizer = CountVectorizer(
        max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
    tf = tfVectorizer.fit_transform(lTweets)
    # extract the names of the features (in our case, the words)
    tfFeatureNames = tfVectorizer.get_feature_names()

    # Run LDA
    ldaModel = LatentDirichletAllocation(
        n_topics=10, max_iter=10, learning_method='online').fit(tf)

    # panel = pyLDAvis.sklearn.prepare(ldaModel, tf, tfVectorizer, mds='tsne')
    # pyLDAvis.show(panel)
    saveTopics(ldaModel, tfFeatureNames, 10, outFileName)


def saveTopics(model, featureNames, numTopWords, outFileName):
    """
    Saves topic id and wrods in those topics in a csv file
    """
    topicFeatures = []
    for topicId, lTopicDist in enumerate(model.components_):
        topicFeatures.append([topicId, " ".join(
            [featureNames[i] for i in lTopicDist.argsort()[:-numTopWords - 1:-1]])])
    topicDF = pd.DataFrame(data=topicFeatures, columns=['TopicId', 'words'])
    topicDF.to_csv(outFileName, index=False)


if __name__ == '__main__':
    main()
