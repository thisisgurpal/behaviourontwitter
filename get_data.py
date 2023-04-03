import pandas as pd
import snscrape.modules.twitter as sntwitter

class DataProcessor():

    # initialise variables
    def __init__(self, user_list, since_date, until_date):
        self.user_list = user_list
        self.since_date = since_date 
        self.until_date = until_date 

    # function to scrape twitter for tweets
    def scrape_twitter(self):

        # array to store tweets
        tweets_list = []

        # get tweets for each user
        for user in self.user_list:
            count = 0

            # get tweets for user
            for tweet in sntwitter.TwitterSearchScraper(f'from:{user} since:{self.since_date} until:{self.until_date}').get_items():
                count = count + 1

                # add tweet to tweets_list array
                tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.user.followersCount, tweet.retweetCount, tweet.likeCount])
                if count == 10:
                    break

        #return dataframe
        return pd.DataFrame(tweets_list, columns=['date', 'id', 'text', 'username', 'followers', 'retweets', 'likes'])
    
    def clean_data(self, data):
        #cleandata
        clean_data = data
        return clean_data
