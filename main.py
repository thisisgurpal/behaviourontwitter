from get_data import DataProcessor
from analysis import Analysis

# variables for scraping tweets
user_list = ['elonmusk', 'katyperry', 'ksi']
since_date = '2022-01-01'
until_date = '2022-03-31'

# initialise DataProcessor class
data_class = DataProcessor(user_list, since_date, until_date)

# scrape twitter for tweets
twitter_data = data_class.scrape_twitter()

# clear scraped data
clean_twitter_date = data_class.clean_data(twitter_data)

# initialise Analysis class
analysis_class = Analysis(clean_twitter_date)

# sentiment analysis
sentiment_data = analysis_class.sentiment_analysis()

# daily freq
daily_tweets_data = analysis_class.daily_freq()

# weekly freq
weekly_tweets_data = analysis_class.weekly_freq()

# engagement
engagement_data = analysis_class.engagement()

# behaviour
behaviour_data = analysis_class.behaviour(daily_tweets_data, weekly_tweets_data, engagement_data)

# cluster analysis
clustered_data = analysis_class.cluster_analysis(behaviour_data)



