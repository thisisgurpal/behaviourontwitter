from get_data import DataProcessor

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

# print data
print(clean_twitter_date)