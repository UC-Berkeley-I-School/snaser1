import random
import numpy as np

class User:
  
    def __init__(self):
        self.__probability = random.uniform(0,1) #probability of clicking an ad 

    def __repr__(self):
        return "this user"

    def __str__(self):
        return "this user"
    
    def show_ad(self):
        r_val = random.random()
        if r_val < self.__probability:
            return True
        else:
            return False
    

class Auction():

    def __init__(self, users, bidders):
        self.users = users
        self.bidders = bidders
        self.balances= {}
        self.balances = {i: 0 for i in range(len(bidders))}
        
        for bidder in range(len(self.balances)):
            self.balances[bidder]= 0

    def execute_round(self):
      #special case: the bidder is less than 2
        if len(self.bidders) < 2:
            return
        #created a local dictionary to hold the bid values
        bidder_dict = {i: 0 for i in range(len(self.bidders))}
        user = random.choice(self.users)
        user_id = self.users.index(user)

        for index, bidder in enumerate(self.bidders):
            value = bidder.bid(user_id)
            bidder_dict[index] = value

        #created a list based on dict.values for sorting
        value_list = list(bidder_dict.values())
        
        #sorted the list and argsort the index, in this case
        #the list contains the bit and the index is the bidder number  
        bidder_list = np.argsort(value_list).tolist()
        value_list = sorted(value_list)
        max_value = value_list[-1]

        # the max_value with multiple bidders
        if value_list.count(max_value) != 1:
            multiple_max_values = []
            multiple_max_bidders = []
            for i in range(len(value_list) - 1, -1, -1):
                if value_list[i] == max_value:
                    multiple_max_values.append(value_list[i])
                    multiple_max_bidders.append(bidder_list[i])
        
            max_bidder = random.choice(multiple_max_bidders)
        else:
            max_bidder = bidder_list[-1]

        winning_price = value_list[-2]

        ad_clicked = user.show_ad()
       
        for index, bidder in enumerate(self.bidders):
            if index == max_bidder:
                if ad_clicked:
                    self.balances[index] += 1
                self.balances[index] -= winning_price
                bidder.notify(True, winning_price, ad_clicked)
            else:
                bidder.notify(False, winning_price, None)


