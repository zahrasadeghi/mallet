# -*- coding: utf-8 -*-
from collections import *
import json
from arabic_reshaper import arabic_reshaper
from persian_wordcloud.wordcloud import PersianWordCloud
from bidi.algorithm import get_display
from PersianStemmer import PersianStemmer
import random
ps = PersianStemmer()


class1file = "data/77.txt"
class2file = "data/84-85.txt"


def randonPartitioner(text, percent):
    firstPartition = text.split(" ")
    partitionedLength = len(firstPartition)
    secondPartiotionLength = int(partitionedLength * percent)
    secondPartiotion = []

    for i in range(secondPartiotionLength):
        r = random.randint(0, partitionedLength -i-1)
        secondPartiotion.append(firstPartition[r])
        del firstPartition[r]
    firstPartitionStringified = ' '.join(firstPartition)
    secondPartiotionStringified = ' '.join(secondPartiotion)
    return firstPartitionStringified, secondPartiotionStringified


def cleanText(text):
    text = text.replace("\n", " ").replace("‌", " ").replace("\r", " ").replace("‎", "").replace("‏", "")
    text = PersianWordCloud.remove_ar(text)
    text = arabic_reshaper.reshape(ps.run(text))
    return text


class1 = open(class1file).read()
class2 = open(class2file).read()
class1 = cleanText(class1)
class2 = cleanText(class2)
# test1, train1 = randonPartitioner(class1, 0.8)
# test2, train2 = randonPartitioner(class2, 0.8)
# print(len(test1), len(train1))
countSentence1 = sum(Counter(class1.split("." and "\n" and "\r" and "?" and "!" and ":")).values())
countSentence2 = sum(Counter(class2.split("." and "\n" and "\r" and "?" and "!" and ":")).values())
sentence1 = class1.split("." and "\n" and "\r" and "?" and "!" and "   " and ":")
sentence2 = class2.split("." and "\n" and "\r" and "?" and "!" and "   " and ":")
print(len(sentence1), len(sentence2))
mallet_text = ""
for i in range(len(sentence2)):
    sentence = sentence2[i].split(" ")
    new_sentence = []
    for j in sentence:
        if len(j)>1:
            new_sentence.append(j)
    print(new_sentence)
    mallet_text = mallet_text + "1385_" + str(i) + " 1385" + " firstWord " + str(new_sentence[0]) + " lastWord " + str(new_sentence[len(new_sentence)-1]) +"\n"

for i in range(len(sentence1)):
    sentence = sentence1[i].split(" ")
    new_sentence = []
    for j in sentence:
        if len(j)>1:
            new_sentence.append(j)
    print(new_sentence)
    if len(new_sentence)>1:
        mallet_text = mallet_text + "1375_" + str(i) + " 1375" + " firstWord " + str(new_sentence[0]) + " lastWord " + str(new_sentence[len(new_sentence)-1])+"\n"
print(mallet_text)
f = open('mallet_text.txt', 'w+')
f.write(mallet_text)
