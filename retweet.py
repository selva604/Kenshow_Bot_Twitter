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

        a = API_._API()
        twitter_list = Kenshow_.gather_Tweet_day(a,w,0)
        
        for i in [a]:
            path = i.SCREEN_NAME
            Kenshow_.csv_write(twitter_list,path,"w")

    if 40 <= time:
        word = "フォロー min_retweets:1000"
    else:
        word = "フォロー min_retweets:500"
    return word

def save(w,path):
    if len(w)>1:
        Kenshow_.csv_write(w,path)

if __name__ == "__main__":

    _api = API_.__API()

    w = make_word()

    for i in [_api]:
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
        
