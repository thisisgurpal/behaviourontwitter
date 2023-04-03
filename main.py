import pandas as pd
import snscrape.modules.twitter as sntwitter

# Set variables for scraping
user_list = ['elonmusk', 'katyperry', 'ksi'] #examples
since_date = '2022-01-01'
until_date = '2022-03-31'
# Scrape tweets
tweets_list = []
for user in user_list:
    count = 0
    for tweet in sntwitter.TwitterSearchScraper(f'from:{user} since:{since_date} until:{until_date}').get_items():
        count = count + 1
        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.user.followersCount, tweet.retweetCount, tweet.likeCount])
        if count == 10:
            break

# Create pandas dataframe
tweets_df = pd.DataFrame(tweets_list, columns=['date', 'id', 'text', 'username', 'followers', 'retweets', 'likes'])

