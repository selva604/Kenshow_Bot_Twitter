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

import API_
import Kenshow_

def make_words():
    dt = datetime.datetime.now()
    dt1 = str(dt.month)+"/"+str(dt.day)
    word = []
    
    for i in [500,1000]:
        word.append("フォロー "+"min_retweets:"+str(i))
        word.append(dt1+" フォロー "+"min_retweets:"+str(i))
        word.append("応募"+" min_retweets:"+str(i))
        word.append("懸賞"+" min_retweets:"+str(i))
    return word
        
if __name__ == "__main__":
    
    word_list = make_words()
    #print(word_list)
    
    Ga_api = API_.Gapo_API()
    Se_api = API_.Selva_API()

    Kenshow_.search(word_list,Ga_api,5)
    Kenshow_.search(word_list,Se_api,5)