# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 12:50:47 2018

@author: user
"""

import re 

#Getting input from user
s = str(input('Enter Paragraph'))
print(s)

a = s.split('.')

no_of_sentences = int(len(a))

#Inserting the sentence in between
a.insert(int(no_of_sentences/2),"UST Global specializes in Healthcare ,Retail & Consumer Goods,Banking,Financial Services,telecom,Media & technology, Insurance,Transportation & Logistocs and Manufacturing & Utilities")

print(a)

no_of_sentences = int(len(a))
#Swapping first and last sentences

first = a[0]
a[0] = a[-1]
a[-1] = first

print(a)

#Removing special characters from the sentence.
s = re.sub('[^A-Za-z0-9]+', ' ', s)

print("After removing special characters")
print (s)


#Counting vowels ,uppercases,lowercases,special . . 

count_vowel = 0
count_upper = 0
count_lower = 0
count_special = 0

for i in str(s):
    if(re.match('^aeiouAEIOU',i)):
        count_vowel = count_vowel+1
    if(i.isupper()):
        count_upper = count_upper+1
    if(i.islower()):
        count_lower = count_lower+1
    
print("Vowels : ",count_vowel)
print("Upper Case : ",count_upper)
print("Lower Case : ",count_lower)

