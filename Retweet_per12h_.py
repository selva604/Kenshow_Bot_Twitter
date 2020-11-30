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

#検索ワード作成
def make_words():
    dt = datetime.datetime.now()
    dt = str(dt.month)+"/"+str(dt.day)

    word = []
    w2 = []
    w3=[]
    w4 = []
    w5 = []
    for i in [1500,2500,5000]:
        word.append(dt+" フォロー "+" min_retweets:"+str(i))
        w2.append("応募"+" min_retweets:"+str(i))
        w3.append("プレゼント"+" min_retweets:"+str(i))
        w4.append("フォロー "+" min_retweets:"+str(i))
        w5.append("懸賞"+" min_retweets:"+str(i))
    return word,w2,w3,w4,w5

def get_API():

    CONSUMER_KEY        = 'xH91alHP35UtPzXw2uiKZkvwa'
    CONSUMER_SECRET_KEY = 'xIZNU469iEuUxD35IHndURywvRc9RWPmCLDN77T7zAIUJMNHJU'
    ACCESS_TOKEN        = '2647079249-4wwsTArYfnujdO9Nkxqy7BMgVf2zmkOGr52lOH6'
    ACCESS_TOKEN_SECRET = 'MLZNeKZvLrssaJYxSsOPgi5MVcWavRqOrqbGcT9S830vx'
    SCREEN_NAME         = 'Selva0604'

    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    return api

#探してリツイート
def search(w1,api):

    #総リツイート数
    c=0
    
    for i in w1:
        print(i)
        if c > 300:
            break
        for status in api.search(q = i,count=20,result_type="mixed"): #recent,popular,mixed
            if c > 300:
                break
            tweet_id = status.id #Tweetのidを取得
            user_id = status.user._json['id'] #ユーザーのidを取得
            
            try:
                api.retweet(tweet_id)# リツイート実行
                api.create_friendship(user_id) #フォローする
                #api.create_favorite(tweet_id) #ファボする
                c+=1

            except:
                #traceback.print_exc()
                continue
    
    print("リツイート:{}".format(c))


if __name__ == "__main__":
    
    t = time.time()
    w1,w2,w3,w4,w5 = make_words()
    api = get_API()
    search(w1,api)
    search(w2,api)
    search(w3,api)
    search(w4,api)
    search(w5,api)
    

    print(time.time()-t)