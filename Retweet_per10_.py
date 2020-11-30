"""
検索オプション
    min_retweets:1000   リツイート数
    since:2017-10-12    ツイートの日付
    until:2020-11-1     指定日まで
    filter:images       画像つき
    filter:links        リンクがある

    応募 min_retweets:100 since:2020-11-1
    11/20 フォロー min_retweets:100
"""

import datetime
import time
import tweepy
import traceback

def make_words():
    dt = datetime.datetime.now()
    dt1 = str(dt.month)+"/"+str(dt.day)
    date = str(dt.month)+"月"+str(dt.day)+"日"
    word = []
    w2 = []
    w3 = []
    w4 = []
    for i in [500,1000]:
        w3.append("フォロー "+"min_retweets:"+str(i))
        word.append(dt1+" フォロー "+"min_retweets:"+str(i))
        w2.append("応募"+" min_retweets:"+str(i))
        w4.append(date+" フォロー "+" min_retweets:"+str(i))
    return word,w2,w3,w4

def get_API():
    CONSUMER_KEY        = ''
    CONSUMER_SECRET_KEY = ''
    ACCESS_TOKEN        = ''
    ACCESS_TOKEN_SECRET = ''
    SCREEN_NAME         = ''

    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    return api

def search(w1,api):
    
    for i in w1:
        for status in api.search(q = i,count=30,result_type="mixed"): #recent,popular,mixed
            tweet_id = status.id #Tweetのidを取得
            user_id = status.user._json['id'] #ユーザーのidを取得
            
            try:
                api.retweet(tweet_id)# リツイート実行
                api.create_friendship(user_id) #フォローする
                #api.create_favorite(tweet_id) #ファボする

            except:
                #traceback.print_exc()
                continue

#PROたちのツイートをリツイート
def retweet_PROs(api):
    list_ID=["kensyou_matome","kensho_twit","potitto_tousen"]

    for id in list_ID:
        results = api.user_timeline(screen_name=id, count=20)
        for status in results:
            tweet_id = status.id #Tweetのidを取得
            user_id = status.user._json['id'] #ユーザーのidを取得
            
            try:
                api.retweet(tweet_id)# リツイート実行
                api.create_friendship(user_id) #フォローする
                #api.create_favorite(tweet_id) #ファボする

            except:
                #traceback.print_exc()
                continue

if __name__ == "__main__":
    
    t = time.time()
    w1,w2,w3,w4 = make_words()
    api = get_API()

    search(w1,api)
    search(w2,api)    
    search(w3,api)
    search(w4,api)
    #retweet_PROs(api)
    
    print(time.time()-t)
