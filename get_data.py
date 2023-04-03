import pandas as pd
import snscrape.modules.twitter as sntwitter

class DataProcessor():

    def __init__(self, user_list, since_date, until_date):
        self.user_list = user_list
        self.since_date = since_date 
        self.until_date = until_date 

    def scrape_twitter(self):
        # Set variables for scraping
        # Scrape tweets
        tweets_list = []
        for user in self.user_list:
            count = 0
            for tweet in sntwitter.TwitterSearchScraper(f'from:{user} since:{self.since_date} until:{self.until_date}').get_items():
                count = count + 1
                tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.user.followersCount, tweet.retweetCount, tweet.likeCount])
                if count == 10:
                    break

        # Create pandas dataframe
        return pd.DataFrame(tweets_list, columns=['date', 'id', 'text', 'username', 'followers', 'retweets', 'likes'])
