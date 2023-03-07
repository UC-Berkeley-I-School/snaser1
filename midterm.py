#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:38:12 2023

@author: sabreenanaser
"""

def count_retweets_by_username(tweet_list):
    """ (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """
    
    # write code here and update return statement with your dictionary
    usernames = []
    for t in tweet_list:
        for i in t.split():
            if i.startswith("@") and i.endswith(":"):
                usernames.append(i.replace("@", "").replace(":",""))
                
    user_dict = {}
    for user in usernames:
        if user in user_dict:
            user_dict[user] += 1
        else:
            user_dict[user] = 1
            
        
    return user_dict




def display(deposits, top, bottom, left, right):
    """display a subgrid of the land, with rows starting at top and up to 
    but not including bottom, and columns starting at left and up to but
    not including right."""
    ans = "" 
    for r in range(top, bottom):
        for c in range(left, right):
            if(r, c) in [(deposit[0], deposit[1]) for deposit in deposits]:
                ans += "X"
            else:
                ans += "-"
        ans += "\n"
    return ans



def tons_inside(deposits, top, bottom, left, right):
    """Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right."""
    
    total = 0
    for r in range(top, bottom):
        for c in range(left, right):
            for dep in deposits:
                if dep[0] == r and dep[1] == c:
                    total += dep[2]
    return total



def birthday_original(dates_list):
    count = 0

    for person_a in dates_list:
        for person_b in dates_list:
            # Make sure we have different people        

            if person_a is person_b:
                continue

            # Check both month and day
            if person_a[0] == person_b[0] and person_a[1] == person_b[1]:
                count += 1
                
    # We counted each pair twice (e.g. jane-bob and bob-jane) so divide by 2:          
    return count//2



def birthday_count(dates_list):
    """Returns the total number of birthday pairs in the dates_list"""
    dates = [(3,14),(2,8),(10,25),(5,17),(3,2),(7,25),(4,30),(8,7),(int(2),8),(1,22)]
    count = 0
    
    length = len(dates)

    for i in range(length):
        for j in range(i+1,length):
            person_a = dates[i]
            person_b = dates[j] 
            if person_a is person_b:
                    continue
            if person_a[0] == person_b[0] and person_a[1] == person_b[1]:
                count += 1
    return count

