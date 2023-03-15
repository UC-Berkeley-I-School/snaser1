#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 6 13:20:27 2023

@author: sabreenanaser
"""
import random


class User:

    def __init__(self):
        self.probability = random.uniform(0,1) #probability of clicking an ad 

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def show_ad(self):
        return random.random() < self.probability 
    #returns true if a random # is less than probability which simulates user clicking on an ad.

class Auction:

    def __init__(self, users, bidders):
        self.users = users
        self.bidders = bidders
        self.id_list
        #self.balances = {i: 0 for i in range(len(bidders))}
        self.balances= {}
        for bidder in range(len(self.balances)):
            self.balances[bidder]= 0
        #self.history = []

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def execute_round(self):
       # user_id = random.randint(0, self.users -1)
       user_id = np.random.choice(self.id_list)
       
       bid_amount= {}
       for bidder in range(len(self.bidders)):
           if self.bidders[bidder].bid(user_id)<0 or self.balances[bidder]<- 1000:
               continue
           else: 
               bid_amount[bidder] = self.bidders[bidder].bid(user_id)
               
               winning_bid = max(bid_amount.values())
        
        #bids = [bidder.bid(user_id) for bidder in self.bidders]
    for bidders, bids in bid_amount.items():
            bids_to_bidders[bids].append(bidders)
            
            for bids, bidders  in bids_to_bidders.items():
                if bids == winning_bid and len(bidders)> 1:
                    winner= np.random.choice(bids_to_bidders(bids))
                
            else:
                winner = bids_to_bidders[bids]
                
            if len(set(bid_amount.values()))>=2:
                second_highest_bid = sorted(set(bid_amount.values()), reverse=True)[-2]
                
            else:
                second_highest_bid = bid_amount[0]
                
            result = self.users[user_id].show_ad()
            
            for bidder in range(len(self.bidders)): 
                if bidder == winner:
                    self.bidders[bidder].notify(True, second_highest_bid, result)
                    if result:
                        self.balances[bidder] +=1
                        self.balances[bidder] -= second_highest_bid
                    else:
                        self.balances[bidder] -=second_highest_bid