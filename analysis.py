import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime, timedelta
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

class Analysis():

    def __init__(self, data):
        self.data = data

    def sentiment_analysis(self):
        # Initialize sentiment analyzer
        sia = SentimentIntensityAnalyzer()

        # Add sentiment analysis scores to dataframe
        sentiment_data = self.data
        sentiment_data['sentiment'] = sentiment_data['text'].map(lambda x: sia.polarity_scores(x)['compound'])

        return sentiment_data

    def daily_freq(self):
        # Calculate daily tweet frequency
        daily_freq_data = self.data
        daily_freq_data['date'] = pd.to_datetime(daily_freq_data['date']).dt.date
        daily_tweets = daily_freq_data.groupby(['username', 'date'])['id'].count().reset_index()
        daily_tweets = daily_tweets.groupby('username')['id'].mean().reset_index(name='daily_tweets')

        return daily_tweets

    def weekly_freq(self):
        # Calculate weekly tweet frequency
        weekly_tweets = self.data
        weekly_tweets['week'] = weekly_tweets['date'].apply(lambda x: (datetime.strptime(str(x), '%Y-%m-%d').date() - timedelta(days=datetime.strptime(str(x), '%Y-%m-%d').weekday())).strftime('%Y-%m-%d'))
        weekly_tweets = weekly_tweets.groupby(['username', 'week'])['id'].count().reset_index()
        weekly_tweets = weekly_tweets.groupby('username')['id'].mean().reset_index(name='weekly_tweets')

        return weekly_tweets

    def engagement(self):
        # Calculate engagement
        engagement = self.data.groupby('username')[['retweets', 'likes']].sum().reset_index()

        return engagement

    def behaviour(self, daily_tweets_data, weekly_tweets_data, engagement_data):
        # Merge behavior metrics into single dataframe
        behavior_df = daily_tweets_data.merge(weekly_tweets_data, on='username').merge(engagement_data, on='username')

        return behavior_df

    def cluster_analysis(self, data):
        # Select columns to use for clustering/PCA
        X = data[['daily_tweets', 'weekly_tweets', 'retweets', 'likes']]

        # Scale data
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Perform PCA
        pca = PCA(n_components=2)
        pca.fit(X_scaled)
        X_pca = pca.transform(X_scaled)

        # Perform clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(X_scaled)
        data['cluster'] = kmeans.labels_

        return data