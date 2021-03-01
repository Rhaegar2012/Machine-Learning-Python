# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:39:37 2021

@author: joseb
"""
'''
Email library test for experimentation 
'''
import email
ham_example = open(r"C:\Users\joseb\Documents\GitHub\Machine-Learning-Python\Spam Classifier\easy_ham\easy_ham\1219.txt", "r")
ham_text=ham_example.read()
em_ham=email.message_from_string(ham_text)
spam_example= open(r"C:\Users\joseb\Documents\GitHub\Machine-Learning-Python\Spam Classifier\spam_2\spam_2\00066.txt")
spam_text=spam_example.read()
em_spam=email.message_from_string(spam_text)
#Message payload test
body_ham=em_ham.get_payload()
body_spam=em_spam.get_payload(decode=False)
def string_transformation(email):
    """
    Input: Email file (as txt) file path
    Output: list of words in the email
    Extracts words from an email file filtering all the characters such as digits
    punctuation and space
    """
    first_stage=email.lower()
    second_stage=first_stage.strip()
    third_stage=second_stage.split()
    for word in third_stage:
        word=''.join(char for char in word if char.isalpha())
    filters=0
    while filters<10:
        for word in third_stage:
            word_index=third_stage.index(word)
            for char in word:
                if char in "1234567890.!@?$_-()[]{},+│/*=:;<>\"":
                    new_word=word.replace(char,"")
                    third_stage[word_index]=new_word
        filters+=1
    return third_stage

def create_bag_of_words(email):
    bag_of_words=[]
    for word in email:
        if (word not in bag_of_words) and (word not in "1234567890.!@?$_-()[]{},+│/*=:;<>\""):
            bag_of_words.append(word)
    return bag_of_words




def get_first_text_part(msg):
    maintype = msg.get_content_maintype()
    if maintype == 'multipart':
        for part in msg.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return msg.get_payload()
print(get_first_text_part(em_ham))