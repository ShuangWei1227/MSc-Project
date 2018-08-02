#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8

import nltk  
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# nltk.download('vader_lexicon')  如果没有这个词典，后面计算score会报错，需要提前下载好
'''
data = ["Great place to be when you are in Bangalore",  
        "The place was being renovated when I visited so the seating was limited",  
        "Loved the ambience, loved the food",  
        "The place is not easy to locate"]
'''

f = open("E:/project/data/分析/Text analytics/wordcount/wordlist_comment.csv", "r")
data = f.readlines()
f.close()

SIA = SentimentIntensityAnalyzer()


sen_score = []

for sentence in data:
    #Return a float for sentiment strength based on the input text. Positive values are positive valence, negative value are negative valence.
    ss = SIA.polarity_scores(sentence)
    #print('{0} {1},'.format(sentence, str(ss)))
    print(ss)



'''
标准化
def normalize(score, alpha=15):
    """
    Normalize the score to be between -1 and 1 using an alpha that
    approximates the max expected value
    """
    norm_score = score/math.sqrt((score*score) + alpha)
    return norm_score
'''
'''
#写入数据
w = open("E1_attribute.csv", "w")
for line in ss_str:
	w.write(str(line))
	w.write('\n')
print('Finish')

'''