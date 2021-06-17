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
        
#create User_Object include the api and the screen name
def Gapo_API():

    CONSUMER_KEY        = 'SRLC9J0BHKPC5i1nMXGmBHGYP'
    CONSUMER_SECRET_KEY = 'D8yjvf85BFr5RmQgr2FFaADnJagvLOcDHG5R035jqOppNcpIus'
    ACCESS_TOKEN        = '1335799921027399682-Y7sCK8CxdR8xovMaEl0G3XZRYYBPX5'
    ACCESS_TOKEN_SECRET = '7atDINzwe01zw1UgE9MV7xJg0ofr2hskoFEDc6w5s9l2c'
    SCREEN_NAME         = 'Gap0rin'
   
    api = get_API(CONSUMER_KEY,CONSUMER_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET) 
    return User_(SCREEN_NAME,api)

def Selva_API():

    CONSUMER_KEY        = '2JMwOGgofortExcV6ANzYvQnp'
    CONSUMER_SECRET_KEY = 'RcOPdMQKb3bgeTOoXDUX4pMx2uQH9gJDnKD2x15KpB9dYM5Sxn'
    ACCESS_TOKEN        = '2647079249-s8O6zrSgYLXgGNK3lADoFSoO0gqjcGD4V0amLQa'
    ACCESS_TOKEN_SECRET = '7hTSKhbQdfU09a0qLzabhTimOlfQWdoZYStpAkByPXkIu'
    SCREEN_NAME         = 'Selva0604'
        
    api = get_API(CONSUMER_KEY,CONSUMER_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    return User_(SCREEN_NAME,api)

def Admiral_API():

    CONSUMER_KEY        = 'PBP9In1yseI4Ylcv8wQOliysa'
    CONSUMER_SECRET_KEY = 'HAu6hD17oBGwTm9jetnkgHhhtTxVjo6eVUHNV9SAW7yf25oo3B'
    ACCESS_TOKEN        = '1345240494276689920-emzsURnPLKoE7MJw1H70dJBVioYICV'
    ACCESS_TOKEN_SECRET = 'cFiBOHFGKB40r7hSg3FlwTgTMeVdaRnwHP9wDR6IHC5Q1'
    SCREEN_NAME         = 'Admiral7012'
        
    api = get_API(CONSUMER_KEY,CONSUMER_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    return User_(SCREEN_NAME,api)

def Note_API():

    CONSUMER_KEY        = 'SA68E6IRMobaJuIvNle8hdjDJ'
    CONSUMER_SECRET_KEY = 'lETnmtygCfcmItdEja0izwNtLs8Ryr3ABOeHb2XgVkpJ5sVuPP'
    ACCESS_TOKEN        = '1367716550115913730-WyWV8qzQAglsF98fYSBiM8npUAL2c8'
    ACCESS_TOKEN_SECRET = '6nOIoJDDtRibzkotldgMg0PVr0KmCdhypx5EeZlpAP6IO'
    SCREEN_NAME         = 'NoticeMan_for'
        
    api = get_API(CONSUMER_KEY,CONSUMER_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    return User_(SCREEN_NAME,api)