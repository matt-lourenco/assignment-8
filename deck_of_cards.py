# Created by: Matthew Lourenco
# Created on: 12 Dec 2016
# This is the class "DeckOfCards"

from cards import *
from numpy import random

class DeckOfCards():
    # This is a deck of cards
    def __init__(self):
        # this method will run on startup
        
        #properties
        self.__card_back = 'card:BackGreen5'
        self.__cards = [Card(1,0), Card(1,1), Card(1,2), Card(1,3), Card(2,4), Card(2,5), Card(2,6), Card(2,7), Card(3,8), Card(3,9), Card(3,10), Card(3,11), Card(4,12), Card(4,13), Card(4,14), Card(4,15), Card(5,16), Card(5,17), Card(5,18), Card(5,19), Card(6,20), Card(6,21), Card(6,22), Card(6,23), Card(7,24), Card(7,25), Card(7,26), Card(7,27), Card(8,28), Card(8,29), Card(8,30), Card(8,31), Card(9,32), Card(9,33), Card(9,34), Card(9,35), Card(10,36), Card(10,37), Card(10,38), Card(10,39), Card(10,40), Card(10,41), Card(10,42), Card(10,43), Card(10,44), Card(10,45), Card(10,46), Card(10,47), Card(10,48), Card(10,49), Card(10,50), Card(10,51)]
        self.__shuffled_cards = []
        self.__player_cards = [self.__cards[0], self.__cards[1], self.__cards[2]]
        self.__computer_cards = [self.__cards[3], self.__cards[4], self.__cards[5]]
        
        self.shuffle()
    
    #getters and setters
    def get_card_back(self):
        #gets the card back property
        return self.__card_back
    def get_player_cards(self):
        #gets the player cards property
        return self.__player_cards
    def get_computer_cards(self):
        #gets the computer cards property
        return self.__computer_cards
    
    def shuffle(self):
        # this method shuffles the array of cards
        for card in range(0, 52):
            selected_card = self.__cards[random.randint(0, len(self.__cards))]
            selected_card.set_card_position(card)
            self.__shuffled_cards.append(selected_card)
            self.__cards.remove(selected_card)
        self.__cards = self.__shuffled_cards
        self.__shuffled_cards = []
        
        #give cards to the player and the computer
        self.__computer_cards = [self.__cards[0], self.__cards[1], self.__cards[2]]
        self.__player_cards = [self.__cards[3], self.__cards[4], self.__cards[5]]
