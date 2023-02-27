#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:00:42 2023

@author: sabreenanaser
"""

import sys
from wordscore import score_word

def has_num(text):
    return any(char.isdigit() for char in text)
    
def run_scrabble(rack1):
    
    rack = 0
    
    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        data = [datum.strip('\n') for datum in raw_input]
    
    if len(rack) < 2:
        return "Needs a rack of up to 7 letters including wildcards: * or ?"
    elif len(rack) > 7:
        return "Too many characters in scrabble rack. Try again."
    elif rack.count("*") > 1 or rack.count("?") > 1:
        return "Too many wildcards. Try again."
    elif has_num(rack):
        return "Contains number. Try again."
    else:
        
        with open("sowpods.txt","r") as infile:
            raw_input = infile.readlines()
            data = [datum.strip('\n') for datum in raw_input]
            
        valid_words = []
        temp = [c for c in rack]
        count = 0
        for char in word:
                if char in temp:
                    count += 1
                    temp.remove(char)
        for char in word:
            for char in temp:
                count = 0
                for char in word:
                    if char in temp:
                        count += 1
                        temp.remove(char)
    elif "*" in temp:
        count += 
        temp.remove("*")
        
    elif "?" in temp:
        count += 1
        temp.remove("?")
        
    if len(word)==count:
        valid_words.append(word)
        +++++++++++++++++++++++++
    for word in valid_word:
        scores_list=[(score_word(word,rack), word)]
        
    return rack