#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8

import nltk  
from nltk.sentiment.vader import SentimentIntensityAnalyzer


'''
data = ["Great place to be when you are in Bangalore",  
        "The place was being renovated when I visited so the seating was limited",  
        "Loved the ambience, loved the food",  
        "The place is not easy to locate"]
'''

f = open("./cleaned_comments_new.csv", "r")
data = f.readlines()
f.close()

SIA = SentimentIntensityAnalyzer()


sen_score = []

for sentence in data:
    #Return a float for sentiment strength based on the input text. Positive values are positive valence, negative value are negative valence.
    ss = SIA.polarity_scores(sentence)
    #print('{0} {1},'.format(sentence, str(ss)))
    print(ss)
