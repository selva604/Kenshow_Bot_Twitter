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
from datetime import date,timedelta

import API_
import Kenshow_

#検索ワード作成
def make_words():
    dt = datetime.datetime.now()
    date = str(dt.month)+"/"+str(dt.day)

    word = []
    
    #現時刻
    time = dt.hour

    #時間帯によって検索日付を変える
    if time == 0:
    
        #基準日
        d = datetime.date(dt.year,dt.month,dt.day)

        #7~b日前 
        before_7days = d - timedelta(days = 1)*7
        u = d - timedelta(days = 1)*6

        w = []
        w.append("フォロー min_retweets:1000 until:"+str(u)+" since:"+str(before_7days))
        
        if dt.month == 12:
            month = 1
        else:
            month = dt.month + 1
        Ga_api = API_.Gapo_API()
        w1 = Kenshow_.gather_Tweet_day(Ga_api,w,month,dt.day)
        print(len(w1))
        Kenshow_.csv_write(w1)


    for i in [1500,3000]:
        word.append(date+" フォロー "+" min_retweets:"+str(i))
        word.append("フォロー "+" min_retweets:"+str(i))
        word.append("懸賞 "+" min_retweets:"+str(i))
        
    return word

if __name__ == "__main__":
    
    word_list = make_words()
    Ga_api = API_.Gapo_API()
    Se_api = API_.Selva_API()
    
    Kenshow_.search(word_list,Se_api,5)
    Kenshow_.search(word_list,Ga_api,5)
    #Kenshow_.retweet_PROs(Se_api,5)

    w = Kenshow_.retweet_CSV(Ga_api)
    w = Kenshow_.retweet_CSV(Se_api)

    if len(w)>=1:
        Kenshow_.csv_write(w)
    

    