import os
import tweepy
import json
from kafka import SimpleProducer, KafkaClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Kafka settings
topic = b'test'
# setting up Kafka producer
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)


#This is a basic listener that just put received tweets to kafka cluster.
class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages(topic, data.encode('utf-8'))
        #print data
        return True

    def on_error(self, status):
        print status

    


if __name__ == "__main__":
    print 'running the twitter-stream python code'
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()

    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET=os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN=os.environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET=os.environ["ACCESS_TOKEN_SECRET"]

    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # api = tweepy.API(auth)
    # auth = OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # stream = Stream(auth, l)
    # Goal is to keep this process always going
    


    # myStream = Stream(auth, myStreamListener)
    stream = Stream(auth, l)
    while True:
        try:
           # stream.sample()
            stream.filter(languages=["en"], track='jeff')
        except:
            pass    
    # myStream.filter(track=['jeff'])# async=True , locations=[33.864554, -84.469070, 33.656192, -84.198532]  , locations=[25.0, -80.0, 48.0, -125.0]