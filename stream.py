import tweepy
import socket
import re
# import preprocessor
import preprocessor as p


# Enter your Twitter keys here!!!
ACCESS_TOKEN = "1322415417638461440-7LsHymm2rcAZwRb7h7yfPjJXqJwd22"
ACCESS_SECRET = "msUlh9xwDBU9TkM1xsLD2UVtnYsVfPKugjiLy7lfTyQon"
CONSUMER_KEY = "dd4dHU4rIAL7LBYFu43q86BRA"
CONSUMER_SECRET = "6ttQ2rdw9v6VjfPOq0OAp3pY7gcKu0Lw7mFV86rsPfK1iqNLjo"


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


hashtag = '#covid19'

TCP_IP = 'localhost'
TCP_PORT = 9001




def preprocessing(tweet):
    tweet = p.clean(tweet)
    # Add here your code to preprocess the tweets and
    # remove Emoji patterns, emoticons, symbols & pictographs, transport & map symbols, flags (iOS), etc
    weirdpattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  
                           u"\U0001F300-\U0001F5FF"  
                           u"\U0001F680-\U0001F6FF"  
                           u"\U0001F1E0-\U0001F1FF"  
                           u"\U00002500-\U00002BEF"  
                           u"\U00002702-\U000027B0"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           u"\u2640-\u2642"
                           u"\u2600-\u2B55"
                           u"\u200d"
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"  
                           u"\u3030"
                           "]+", flags=re.UNICODE)
    tweet = weirdpattern.sub(r'', tweet)
    return tweet




def getTweet(status):

    # You can explore fields/data other than location and the tweet itself.
    # Check what else you could explore in terms of data inside Status object

    tweet = ""
    location = ""

    location = status.user.location

    if hasattr(status, "retweeted_status"):  # Check if Retweet
        try:
            tweet = status.retweeted_status.extended_tweet["full_text"]
        except AttributeError:
            tweet = status.retweeted_status.text
    else:
        try:
            tweet = status.extended_tweet["full_text"]
        except AttributeError:
            tweet = status.text

    return location, preprocessing(tweet)





# create sockets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        location, tweet = getTweet(status)

        if (location != None and tweet != None):
            tweetLocation = location + "::" + tweet+"\n"
            print(status.text)
            conn.send(tweetLocation.encode('utf-8'))

        return True


    def on_error(self, status_code):
        if status_code == 420:
            print("Code 420")
            return False
        else:
            print(status_code)

myStream = tweepy.Stream(auth=auth, listener=MyStreamListener())
myStream.filter(track=[hashtag], languages=["en"])
