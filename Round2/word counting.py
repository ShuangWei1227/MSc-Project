#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8


import re  

f = open("./cleaned_surveydata/cleaned_survey2_visualaids.csv", "r")
data = f.readlines()
f.close()


dictResult = {}  
  
# Find the letters each line  
for line in data:
	listMatch = re.findall('[a-zA-Z]+', line.lower())
	for eachLetter in listMatch:
		eachLetterCount = len(re.findall(eachLetter, line.lower()))
		dictResult[eachLetter] = dictResult.get(eachLetter, 0) + eachLetterCount

  
# Sort the result  
result = sorted(dictResult.items(), key=lambda d: d[1], reverse=True)  


#word_num = []
for i in range(len(result)):
    word, count=result[i]
    print('{0},{1}'.format(word, count))
    #word_num += (word, count)

