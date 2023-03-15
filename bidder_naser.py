#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 6 13:25:55 2023

@author: sabreenanaser
"""

class Bidder:

    def __init__(self, num_users, num_rounds):
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.history = {}
        self.balance = 0
        

    def __repr__(self): 
        return "bidder"
        

    def __str__(self):
        return "bidder"

    def bid(self, user_id):
        
        self.base_bid=3
        
        if self.balance <= -1000:
            return 0 #Out of money
        
        self.user_id=user_id
        
        if self.user_id not in self.history.keys():
            self.history[self.user_id]=self.base_bid
            return self.base_bid
        elif self.user_id in self.history.keys() and self.history[self.user_id] > self.base_bid:
            return self.history[self.user_id]
        
        else:
            return self.base_bid
        
        

    def notify(self, auction_winner, price, clicked):
        
        self.auction_winner = auction_winner
        self.price = price
        self.clicked = clicked
        
        if self.price>self.base_bid:
            self.history[self.user_id] = self.price
            
        else: 
            self.history[self.user_id]=self.base_bid
        
        
        
        if auction_winner == True:
            if clicked: self.balance += 1 - price
        else:
            self.balance -= price
            
    def get_balance(self): 
        return self.balance
        