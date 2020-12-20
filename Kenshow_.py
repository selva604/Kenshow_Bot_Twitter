import datetime
import tweepy
import traceback
import re
import csv

import API_

#フォロー解除
def rm_follow(User_,n):
    api = User_.api
    name = User_.SCREEN_NAME

    follow = api.friends_ids(name)

    #古い順にフォロー解除
    for f in follow [:-n:-1]:
        print("ID:{}のフォローを解除しました。".format(api.get_user(f).screen_name))
        api.destroy_friendship(f)


#プロフィールのリンクをみて怪しいユーザをはじく
def filter(api,user_id):
    user = api.get_user(user_id)

    try:
        url = user.entities["url"]["urls"][0]["expanded_url"]
        #print(url)
    except:
        return 0
    
    NG_Link=["amazon","lin.ee","youtube.com","twitcasting.tv","mildom.com","mirrativ.com"]

    if url == None:
        return 0
    #NG_Linkがあったら1を返す
    for word in NG_Link:
        if word in url:
            return 1
        
        else:
            continue
    return 0

#ツイートを検索
def search(word_list,User_,c):
    api = User_.api
    
    for word in word_list:
        for status in api.search(q = word,count=c,result_type="recent"): #recent,popular,mixed
            tweet_id = status.id                                         #Tweetのidを取得
            user_id = status.user._json['id']                            #ユーザーのidを取得
            
            if filter(api,user_id) > 0:
                continue
            try:
                User_.api.retweet(tweet_id)                              #リツイート実行
                User_.api.create_friendship(user_id)                     #フォローする
                #api.create_favorite(tweet_id)                           #ファボする

            except:
                #traceback.print_exc()
                continue

#懸賞リツイートするユーザをリツイート
def retweet_PROs(User_,c):
    list_ID=["potitto_tousen","kensyou_matome","kensho_twit"]
        
    for id_ in list_ID:
        for status in tweepy.Cursor(User_.api.user_timeline,id=id_).items(c):
            tweet_id = status.id #Tweetのidを取得
            user_id = status.user._json['id'] #ユーザーのidを取得
            text = status.text
            try:
                #懸賞 retweet を検索
                if "RT @" in text:
                    User_.api.retweet(tweet_id) # リツイート実行
                    User_.create_friendship(user_id) # フォローする
                    #api.create_favorite(tweet_id)  # ファボする

            except:
                #traceback.print_exc()
                continue

#指定した日付のツイートを集めてCSVに書き込む
def gather_Tweet_day(User_,word_,next_month,days):
    
    #tweetを収納するリスト
    tweets_data=[]
    g = ["/","月"]
    
    for tweet in tweepy.Cursor(User_.api.search, q=word_,tweet_mode='extended',lang='ja').items(1000):
    #つぶやきテキスト(FULL)を取得
        for i in g:
            a = '([0-9]{1,2})'+i+'([0-9]{1,2})'
            try:
                m = re.search(a, tweet.full_text, flags=re.DOTALL)
                month = m.group(1)
                day = m.group(2)
                if int(month)==next_month:
                    tweets_data.append([tweet.id,tweet.user.screen_name])
                elif int(day)>=days:
                    tweets_data.append([tweet.id,tweet.user.screen_name])
            except:
                continue
        
    return tweets_data

def retweet_CSV(User_):
    w=[]
    try:
        with open("twitter.csv") as f:
            reader = csv.reader(f)
            for i,row in enumerate(reader):
                if i >= 10:
                    w.append(row)
                    continue
                try:
                    User_.api.retweet(row[0])
                    User_.api.create_friendship(row[1])
                except:
                    #print(row)
                    continue
    except:
        print("error")
    return w

def csv_write(tweets_data):
    try:
        with open("twitter.csv",'w',newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            for i in tweets_data:
                writer.writerow(i)
    except:
        print("error")
if __name__=="__main__":
    word_ = "フォロー min_retweets:1000 until:2020-12-10 since:2020-12-09"
    Gapo = API_.Selva_API()

    
    