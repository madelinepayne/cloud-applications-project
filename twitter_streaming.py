#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "925901916512641026-IMcQ5hTUfyfZp0hAWxBjKDPQxhmfdHE"
access_token_secret = "FYLFqjWgxvcycDhQl9I16bhwz4Hk7iHyuvxOgIq76QH7W"
consumer_key = "HY3HknvpInVkE1ZvYkJKrbuXL"
consumer_secret = "cik2gh2BKduNfbk1hE3eOe2HfAW3gdkniGtitmTYZvPive6ViR"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])