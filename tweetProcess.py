from nltk.tokenize import TweetTokenizer
import re
def TweetProcess(text, tokeniser=TweetTokenizer(), stopwords=[], pattern='http'):
  regexPattern = {
    'all': '^((http(s)?://)|@|#)',
    'http': 'http(s)?://',
    'hashtag': '^#',
    'username': '^@'
  }
  lText = text.lower()
  tokens = tokeniser.tokenize(lText)
  return [tok for tok in tokens if tok not in stopwords and not tok.isdigit() and not re.match(regexPattern[pattern], tok)]
