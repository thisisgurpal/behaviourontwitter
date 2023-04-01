import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "sarcasm (#sarcasm) lang:en since:2023-03-01"
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.rawContent])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])

print(df)