import os 
import tweepy
from pprint import pprint

CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET=os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN=os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET=os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
# api.update_status('tweepy + oauth!')
######################################
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text
######################################
######################################
# Get the User object for twitter...
# user = api.get_user('twitter')
# print user.screen_name
# print user.followers_count
# for friend in user.friends():
#     print friend.screen_name
######################################
for status in tweepy.Cursor(api.user_timeline).items():
    # process status here
    pprint(status.text)
    print type(status)