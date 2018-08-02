#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8


import re  

f = open("E:/project/data/分析/Text analytics/cleaned_data/cleaned_survey2_3.csv", "r")
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


#写入
'''
w = open("wordcount.csv", "w")

for line in result:
	w.write(str(line))
	w.write('\n')
'''


'''
with open('./cleaned_data/cleaned_survey1_2.csv', 'r') as f:  
    dictResult = {}  
  
    # Find the letters each line  
    for line in f.readlines():  
        listMatch = re.findall('[a-zA-Z]+', line.lower()) # remember to lower the letters  
  
    # Count  
        for eachLetter in listMatch:  
            eachLetterCount = len(re.findall(eachLetter, line.lower()))  
            dictResult[eachLetter] = dictResult.get(eachLetter, 0) + eachLetterCount  
  
    # Sort the result  
    result = sorted(dictResult.items(), key=lambda d: d[1], reverse=True)  
    #for each in result:  
    #    print(each)

    w = open("wordcount.csv", "w")

    for line in wordcount:
	w.write(str(line))
	w.write('\n')

    for i in range(len(result)):
    	word,count=result[i]
    	print('{0},{1}'.format(word, count))


'''


'''
def getText():
	txt=open('./cleaned_data/cleaned_survey1_2.csv','r').read()
	txt=txt.lower()

    for ch in '~!@#$%^&*()_+"{}[]|?.<>?':
    	txt=txt.replace(ch,"")
    return txt

hamletTxt=getText()
words=hamletTxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

for i in range (10): ###这里就让它输出10个看看得了
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
'''