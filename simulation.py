# umpire 
#   u - stimulating how a virus spreads through a population over time
#   m - plannign to use:
#           - oop to represent people
#           - randomness to simulate the spread of a virus
#           - loops to stimulate days passing
#           - matplotlib to visualize how things change over time
#   p - person class, sim class, run sim, plot results 

import random 

class Person:
    def __init__(self):
        # person starts as healthy and not infected
        self.state = "healthy"
        self.days_infected = 0
    
    # infect person 
    def infect(self):
        if self.state == "healthy" # person will only be infected if not already
            self.state = "infected"
            
    # update person status everyday 
    def update(self):
        if self.state == "infected":
            self.days_infected += 1 # how many days theyve been sick
            if self.days_infected >= 7:
                self.state = "recovered" # person will recover after 7 days 