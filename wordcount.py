#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8


f = open("cleaned_comment.csv", "r")
data = f.read()
f.close()

#print(data)

words = data.split(" ")

#print(words)

#总单词数
#print("The words in the text are:")
#print(words)
num_words = len(words)
print("The number of words is ", num_words)

#总行数
lines = data.split("\n")
#print("The lines in the text are:")

print("The number of lines is", len(lines)-1)

print(lines)

wordcount = []

#每行单词数
for _ in lines[:-1]:
	i = str(_).split(' ')
	#print(i)
	c = len(i)
	wordcount.append(c)
print(wordcount)

#写入数据
w = open("wordcount.csv", "w")
for line in wordcount:
	w.write(str(line))
	w.write('\n')
print('Finish')