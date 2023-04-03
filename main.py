from get_data import DataProcessor

user_list = ['elonmusk', 'katyperry', 'ksi']
since_date = '2022-01-01'
until_date = '2022-03-31'
data_class = DataProcessor(user_list, since_date, until_date)


twitter_data = data_class.scrape_twitter()

print(twitter_data)