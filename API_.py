import tweepy
import datetime

class User_:
    def __init__(self,name,api_,count=0,mode = 0):
        self.SCREEN_NAME = name
        self.api = api_
        self.count = 0
        self.mode = 0

        dt = datetime.datetime.now()
        # mode = 0 stop
        if  1 < dt.hour < 7:
            self.mode = 0
        elif dt.minute == 0 or 40:
            self.mode = 1
        elif dt.minute == 20:
            self.mode = 2
        else:
            self.mode = 3
#get API
def get_API(CONSUMER_KEY,CONSUMER_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET):
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    return tweepy.API(auth,wait_on_rate_limit=True)

def Selva_API():

    CONSUMER_KEY        = ''
    CONSUMER_SECRET_KEY = ''
    ACCESS_TOKEN        = ''
    ACCESS_TOKEN_SECRET = ''
    SCREEN_NAME         = ''
        
    api = get_API(CONSUMER_KEY,CONSUMER_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    return User_(SCREEN_NAME,api)
