"""
検索オプション
    min_retweets:1000   リツイート数
    since:2017-10-12    ツイートの日付
    filter:images       画像つき
    filter:links        リンクがある
"""

import tweepy
import traceback

CONSUMER_KEY        = ''
CONSUMER_SECRET_KEY = ''
ACCESS_TOKEN        = ''
ACCESS_TOKEN_SECRET = ''
SCREEN_NAME         = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#ツイート内容
q_word="11/18 リツイート -filter:retweets"

#総リツイート数
c=0

for status in api.search(q=q_word,count=5):
    tweet_id = status.id #Tweetのidを取得
    user_id = status.user._json['id'] #ユーザーのidを取得

    try:
        api.retweet(tweet_id)# リツイート実行
        api.create_friendship(user_id) #フォローする
        #api.create_favorite(tweet_id) #ファボする

        c+=1
    except:
        traceback.print_exc()

print("リツイート:{}".format(c))
