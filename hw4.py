#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 03:26:29 2021

@author: lesliecastelan

Professor: Hangjie Ji
Discussion: 3B
"""

#%%
import re
import urllib
from happiness_dictionary import happiness_dictionary



#%%

def mytype(v):
    """
    Finds the data type of input object.
    
    Returns string describing data type.

    """
    input = str(v)
    #print("Input:",input)
    if re.search(r'^(-)?(\d+)$',input): #without the $ it will recognize a list of ints 
        return "int"                 #up to before the bracket and call it int
                                    #without the ^ will start reading float after the period
    elif re.search(r'^(-)?\d+\.\d+',input):
        return "float"
    elif re.search(r'^(\[).*(\])$',input): 
        return "list"
    else:
        return "string"
    
# print(mytype([1, 2, 3]))
# print(mytype([]))
# print(mytype(-020202.25))
# print(mytype({1,2}))
    
#%%


def findpdfs(L):
    """
    Finds all PDF files within list. 
    
    Returns list of filenames with that format.
    
    """
    found_list =[]
    for names in L:
        if re.search(r'^[A-Za-z0-9]+\.pdf',names): 
            found_list.append(re.search(r'^[A-Za-z0-9]+\.pdf',names).group())
    return found_list


# P = ["IMG2309.jpg", "homework.py", "lecture1.pdf"]
# L = ["IMG2309.jpg", "lecture1.pdf", "homework.py", "homework2.pdf"]
# print(findpdfs(P))
# print(findpdfs(L))
#Z="IMG2309.jpg"
#K="lecture1.pdf"
#print(re.findall(r'^[A-Za-z0-9]+\.pdf',Z))#returns empty list if doesn't find anything 
#print(re.findall(r'^[A-Za-z0-9]+\.pdf',K)) #returns ['lecture1.pdf']
#matched_list =re.findall(r'^[A-Za-z0-9]+\.pdf',K)
#print(matched_list[0]) #ensure that ACTUAL list object returned 
# print(re.findall(r'^[A-Za-z0-9]+\.pdf',P)) #cannot do this since P is list not string 

#print(re.search(r'^[A-Za-z0-9]+\.pdf',K).group())
#print(re.search(r'^[A-Za-z0-9]+\.pdf',Z).group()) cannot return a Nonetype with group()

#%%

def findemail(url):
    """
    Finds all emails within a page. 
    
    Returns all found emails within a list. 
    """
    page=str(urllib.request.urlopen(url).read().decode())
    emails= []
    if re.search(r'[A-Za-z0-9]+@math\.ucla\.edu',page):
        emails.append(re.search(r'[A-Za-z0-9]+@math\.ucla\.edu',page).group())
        
    if re.search(r'[A-Za-z0-9]+\sAT\smath\sDOT\sucla\sDOT\sedu',page):
        emails.append(re.search(r'[A-Za-z0-9]+\sAT\smath\sDOT\sucla\sDOT\sedu',page).group())
        
    if re.search(r'[A-Za-z0-9]+\sat\smath\sdot\sucla\sdot\sedu',page):
        emails.append(re.search(r'[A-Za-z0-9]+\sat\smath\sdot\sucla\sdot\sedu',page).group())
        
    if re.search(r'[A-Za-z0-9]+\[AT\]ucla\[DOT\]edu',page):
        emails.append(re.search(r'[A-Za-z0-9]+\[AT\]ucla\[DOT\]edu',page).group())
        
    if re.search(r'[A-Za-z0-9]+\[at\]ucla\[dot\]edu',page):
        emails.append(re.search(r'[A-Za-z0-9]+\[at\]ucla\[dot\]edu',page).group())
        
    if re.search(r'[A-Za-z0-9]{3}@[A-Za-z0-9]{3}\.[A-Za-z0-9]{3}\.[A-Za-z0-9]{3}',page):
        emails.append(re.search(r'[A-Za-z0-9]{3}@[A-Za-z0-9]{3}\.[A-Za-z0-9]{3}\.[A-Za-z0-9]{3}',page).group())
    
    return emails 

#url1 = "https://www.math.ucla.edu/~hangjie/contact/"
#url2 = "https://www.math.ucla.edu/~hangjie/teaching/Winter2019PIC16/regexTest"
#print(findemail(url1)) 
#print(findemail(url2))

#%%

def happiness(text):
    """
    Finds the average happiness score of an input string
    by finding words in happiness_dictionary.
    
    Returns a float of the happiness score of input string.

    """
    words_found=0
    total_score=0.0
    
    words_in_text= re.findall(r'\w+',text)
    for word in words_in_text:
        word=word.lower()
        for key,score in happiness_dictionary.items():
            if word == key:
                words_found+=1
                total_score+=score #check if possible: print(type(score))
                #print(key,score)
    return total_score/words_found

#texth="Leslie is cool"
# s1 = "Mary had a little lamb."
# s2 = "Mary had a little lamb. Mary had a little lamb!"
# s3 = "A quick brown fox jumps over a lazy dog."
# print(happiness(s1))
# print(happiness(s2))
# print(happiness(s3))

