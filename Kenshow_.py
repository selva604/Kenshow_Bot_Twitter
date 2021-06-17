import datetime
import tweepy
import traceback
import re
import csv
import time

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


#怪しいユーザをはじく
#Tweet内容に準じてはじく 日付を超えていたり，お金配り系，
def filter(api,user_id):
    user = api.get_user(user_id)

    try:
        url = user.entities["url"]["urls"][0]["expanded_url"]
        #print(url)
    except:
        return 1
    
    # NG_Link=["amazon","youtube.com","twitcasting.tv","mildom.com","mirrativ.com"]

    # if url == None:
    #     return 1
    
    # #NG_Linkがあったら1を返す
    # for word in NG_Link:
    #     if word in url:
    #         return 1
        
    #     else:
    #         continue
    return 0

#ツイートを検索
def search(word,User_,c):
    api = User_.api
    
    for status in api.search(q = word,count=c,result_type="recent"): #recent,popular,mixed
        if User_.count >= 10:
            return 0
        
        tweet_id = status.id                                         #Tweetのidを取得
        user_id = status.user._json['id']                            #ユーザーのidを取得
            
        text = status.text
        #get screen_name in text
        name_list = re.findall('@[a-zA-Z0-9_]*', text)

        if len(name_list) > 1:
            continue
        # elif filter(api,user_id) > 0:
        #     continue

        try:
            User_.api.retweet(tweet_id)                              #リツイート実行
            User_.count+=1
            time.sleep(20)
                
            for screen_ in name_list:
                try:
                    User_.api.create_friendship(screen_)
                except:
                    continue

            User_.api.create_friendship(user_id)                     #フォローする
            #api.create_favorite(tweet_id)                           #ファボする

        except:
            #traceback.print_exc()
            continue
            

#懸賞リツイートするユーザをリツイート
def retweet_PROs(User_,c):
    list_ID=["potitto_tousen","kensho_twit"]
        
    for id_ in list_ID:
        for status in tweepy.Cursor(User_.api.user_timeline,id=id_).items(c):
            if User_.count >= 10:
                return 0
            tweet_id = status.id #Tweetのidを取得
            user_id = status.user._json['id'] #ユーザーのidを取得
            text = status.text
            try:
                #懸賞 retweet を検索
                if "RT @" in text:
                    User_.api.retweet(tweet_id) # リツイート実行
                    User_.count += 1
                    time.sleep(30)
                    User_.api.create_friendship(user_id) # フォローする
                    #api.create_favorite(tweet_id)  # ファボする

            except:
                #traceback.print_exc()
                continue

#指定した日付のツイートを集めてCSVに書き込む
def gather_Tweet_day(User_,word_,mode):
    dt = datetime.datetime.now()
    
    #tweetを収納するリスト
    tweets_data=[]
    if mode == 0:
        a = '([0-9]{1,2})/([0-9]{1,2})'
        b = '[0-9]/'
    else:
        a = '([0-9]{1,2})月([0-9]{1,2})日'
        b = '[0-9]年'

    for tweet in tweepy.Cursor(User_.api.search, q=word_,result_type="recent",tweet_mode='extended',lang='ja').items(500):
    #つぶやきテキスト(FULL)を取得
        user_id = tweet.user._json['id']                            #ユーザーのidを取得

        text = tweet.full_text
        #print(text)
        #get screen_name in text
        name_list = re.findall('@[a-zA-Z0-9_]*', text)

        if len(name_list) > 1:
            continue
        
        try:
            if str(dt.year) in text:
                c = b + a
            else:
                c = a
    
            #get date in text 
            date_list  = re.findall(c,tweet.full_text)
            for date in date_list:
                #print(date)
                if int(date[0])== dt.month and int(date[1]) < dt.day:
                    #print(month_,days)
                    break
                
                elif int(date[0]) == dt.month - 1 :
                    break

            else:
                tweets_data.append([tweet.id,tweet.user.screen_name])
                #print('save')
        except:
            continue
            #tweets_data.append([tweet.id,tweet.user.screen_name])

    return tweets_data

def retweet_CSV(User_):
    w=[]
    dt_now = datetime.datetime.now()
    hour = dt_now.hour
    if hour in [0,8,10,12,15,17,19,21]:
        count = 8
    else:
        count = 6
    try:
        with open("twitter_"+User_.SCREEN_NAME+".csv") as f:
            reader = csv.reader(f)
            
            for i,row in enumerate(reader):
                if User_.count >= count:
                    w.append(row)
                    continue
                try:
                    User_.api.retweet(row[0])
                    User_.count += 1
                    time.sleep(20)
                    User_.api.create_friendship(row[1])
                except:
                    #print(row)
                    continue
                
    except:
        print("error")
    return w

def csv_write(tweets_data,path,mode_ = "w"):
    try:
        with open("twitter_"+path+".csv",mode = mode_,newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            for i in tweets_data:
                writer.writerow(i)
    except:
        print("error")

if __name__=="__main__":
    dt = datetime.datetime.now()
    if 1 in [12,17,2]:
        print(dt)
    t1 ="2021年3/1 24:0124/44 5.51"
    t2 = '4 3/2 しめきり　４・２55/5'
    
    a = '([0-9]{1,2})/([0-9]{1,2})'
    # date_list  = re.findall(a,t2)
    # print(date_list)
    # c = []
    # for j in [t1,t2]:
    #     if str(dt.year) in j:
    #         a = '[0-9]年([0-9]{1,2})/([0-9]{1,2})'
    #     else:
    #         a = '([0-9]{1,2})/([0-9]{1,2})'
    #     date_list  = re.findall(a,j)
    #     for i in date_list:
    #         print(i)
    #         if int(i[0]) == 3 and int(i[1]) < 2:
    #             print(j)
    #             break

    #     else:
    #         c.append(j)
    #         continue
    # print(c)
            
    


