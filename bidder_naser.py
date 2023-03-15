import random

class Bidder:
    
    def __init__(self, num_users, num_rounds):
        self.num_users = num_users
        self.num_rounds = num_rounds
                
    def __repr__(self): 
        return "This bidder"
        
    def __str__(self):
        return "This bidder"

    def bid(self, user_id):
        amount = random.uniform(0, 1000)
        return round(amount, 3)

    def notify(self, auction_winner, price, clicked = None):
        #user send info to bidder
        if(auction_winner):
            print("You are the winner of this round")
        else:
            print("You are not the winner")
        
        print("The winning price is", price)

        if(clicked):
            print("The user clicked your ad")

        return auction_winner, price, clicked
        