#
# COSC2671 Social Media and Network Analytics
# @author Jeffrey Chan, 2018
#

import sys
import tweepy as tw


def twitterAuth():
    """
        Setup Twitter API authentication.
        Replace keys and secrets with your own.

        @returns: tweepy.OAuthHandler object
    """

    try:
        # Fake values entered in submission
        consumerKey = "j2BqhBSbauXHstCUmSRo9aSG0"
        consumerSecret = "oYSQMcD16UbfDJvFWgaDQxGFcP1slUggVsd0Gbs29O4aB4omSf"
        accessToken = "495006840-OL6CEzw0P3tUX05r2BZVFl31tpn6qsZtdRBqu2fK"
        accessSecret = "f6obWb6KlIURnY77Rq3VPngA0AeSsBlr8dPBlyp2MEPrk"
    except KeyError:
        sys.stderr.write("Key or secret token are invalid.\n")
        sys.exit(1)

    auth = tw.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessSecret)

    return auth



def twitterClient():
    """
        Setup Twitter API client.

        @returns: tweepy.API object
    """

    auth = twitterAuth()
    client = tw.API(auth)

    return client
