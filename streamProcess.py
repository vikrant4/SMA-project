import json
import re

def main():
  """
  Used to move tweets from the streaming API to json files of respective cities and
  combine all the tweets into a single json file names all.json.
  """
  melbRegex = "(mel)|(vic)"
  sydnRegex = "(syd)|(new)|(nsw)"

  # Adding all tweets from melbourne.json to all.json
  with open('melbourne.json', 'r') as m, open('all.json', 'a') as a:
    for line in m:
      a.write(line)
  
  # Adding all tweets from sydney.json to all.json
  with open('sydney.json', 'r') as s, open('all.json', 'a') as a:
    for line in s:
      a.write(line)
  # Adding all tweets from brisbane.json to all.json
  with open('brisbane.json', 'r') as b, open('all.json', 'a') as a:
    for line in b:
      a.write(line)
  # Adding all tweets from streamAus.json to all.json and to respective cities' files
  with open('streamAus.json', 'r') as r, open('melbourne.json', 'a') as m, open('sydney.json', 'a') as s, open('other.json', 'w') as o, open('all.json', 'a') as a:
    for line in r:
      if len(line) <= 2:
        continue
      tweet = json.loads(line)
      try:
        location = tweet.get('user', '')['location']
        if location and re.match(melbRegex, location, re.IGNORECASE):
          m.write(line)
        elif location and re.match(sydnRegex, location, re.IGNORECASE):
          s.write(line)
        else:
          o.write(line)
      except Exception as e:
        print(e)
        o.write(line)
      finally:
        a.write(line)



if __name__ == '__main__':
  main()
