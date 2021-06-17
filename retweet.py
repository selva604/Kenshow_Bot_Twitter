import time
import datetime

import API_
import Kenshow_
from datetime import date,timedelta

def make_word():
    dt = datetime.datetime.now()
    hour = dt.hour
    time = dt.minute

    if hour == 2 and 15 <= time <= 20:
        d = datetime.date(dt.year,dt.month,dt.day)
        #7~b日前 
        next_ = d + timedelta(days = 1)

        w = str(d.month)+"/"+str(d.day) + " フォロー min_retweets:400"
        w1 = "フォロー min_retweets:500"
        w2 = str(d.month)+"月"+str(d.day)+"日 フォロー min_retweets:400"

        print(w)
        G = API_.Gapo_API()
        twitter_list = Kenshow_.gather_Tweet_day(G,w,0)
        print(len(twitter_list))

        S = API_.Selva_API()
        #twitter_list1 = Kenshow_.gather_Tweet_day(S,w1,0)
        
        A = API_.Admiral_API()
        twitter_list2 = Kenshow_.gather_Tweet_day(A,w2,1)
        print(len(twitter_list2))

        for i in [G,S,A]:
            path = i.SCREEN_NAME
            Kenshow_.csv_write(twitter_list,path,"w")
            Kenshow_.csv_write(twitter_list2,path,"a")
            #Kenshow_.csv_write(twitter_list1,path,"a")

    if 40 <= time:
        word = "フォロー min_retweets:1000"
    else:
        word = "フォロー min_retweets:500"
    return word

def save(w,path):
    if len(w)>1:
        Kenshow_.csv_write(w,path)

if __name__ == "__main__":

    Ga_api = API_.Gapo_API()
    Se_api = API_.Selva_API()
    Ad_api = API_.Admiral_API()

    w = make_word()

    for i in [Se_api,Ad_api,Ga_api]:
        if i.mode == 0:
            Kenshow_.rm_follow(i,5)
            continue
        else:
            Kenshow_.search(w,i,5)
            
            if i.mode == 1:
                csv = Kenshow_.retweet_CSV(i)
                save(csv,i.SCREEN_NAME)
                print("a")
            
            elif i.mode == 2:
                #Kenshow_.retweet_PROs(i,10-i.count)
                print("a")
            
    # Kenshow_.search(w,Ad_api,3)
    # Kenshow_.search(w,Ga_api,3)
    # Kenshow_.search(w,Se_api,3)
