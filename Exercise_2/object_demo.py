# File name: object_demo.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing demonstration for using objects

import random

class Coin:
    def __init__(self):
        self.sideup = "Heads"
        
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"
            
    def get_sideup(self):
        return self.sideup
    
def main():
    my_coin = Coin()
    strangers_coin = Coin()
    
    print("State of my coin:")
    print(my_coin.get_sideup())
    print("State of strangers coin:")
    print(strangers_coin.get_sideup())
    
    
    my_coin.toss()
    strangers_coin.toss()
    
    print("\nNew state of my coin:")
    print(my_coin.get_sideup())
    print("New state of strangers coin:")
    print(strangers_coin.get_sideup())
    

main()