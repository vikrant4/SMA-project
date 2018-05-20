import sys
import string
import time
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitterClient import twitterAuth


def main():
    """
    Usage: twitterStreaming.py [out filename (json)] <list of query terms>
    Example:
    python twitterStreaming.py streamAus.json gov government tax taxes budget minister federal politics ethics ethical sustainable tourism racism poverty gdp income job
    To gather tweets that have keywords "rmit", "#rmit_csit", "cs"

    To stop collecting, just stop the script.
    """
    # read in from command line all the terms that we will filter the stream on
    assert(len(sys.argv) > 2)
    sOutFilename = sys.argv[1]
    sQuery = sys.argv[2:]

    # output file is the input file name with all the query terms and '.txt'
    auth = twitterAuth()
    # open up the stream
    twitterStream = Stream(auth, CustomListener(sOutFilename, sQuery))
    # filter out tweets not of query word
    twitterStream.filter(locations=[111.9, -44.1, 154.9, -10.9], async=True)


class CustomListener(StreamListener):
    """
    Listener that calls on_data when a new tweet appears.
    """


    def __init__(self, fName, wordList):
        self.outFile = fName
        self.timeToSleep = 10
        self.wordList = set(wordList)


    def on_data(self, raw_data):
        try:
            with open(self.outFile, 'a') as f:
                tweetTextWords = json.loads(raw_data)['text'].split(' ')
                if bool(self.wordList & set(tweetTextWords)):
                    f.write(raw_data)
                return True

        except BaseException as e:
            sys.stderr.write("Error on_data: {}\n.format(e)")
            time.sleep(self.timeToSleep)

        return True


    def on_error(self, status):
        if status == 420:
            sys.stderr.write("Rate limit exceeded\n")
            return False
        else:
            sys.stderr.write("Error {}\n".format(status))
            return True


def format_filename(fName):
    """
    Conver all irrelevant characters from the input filename.
    """
    lValidChars = "-_." + string.ascii_letters + string.digits

    return ''.join(oneChar for oneChar in fName for oneChar in lValidChars)



if __name__ == '__main__':
    main()
