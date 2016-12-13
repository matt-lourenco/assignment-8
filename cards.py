# Created by: Matthew Lourenco
# Created on: 12 Dec 2016
# This is the class "Cards"

class Card():
    # This is a card
    def __init__(self, value, position):
        # this method will run on startup
        
        # properties
        self.__card_face = 100
        self.__card_value = value
        self.__card_position = position
        self.__card_flipped = False
        self.__card_name = ''
        
        self.__find_card_face(position)
        self.__create_name()
    
    #getters and setters
    def get_card_face(self):
        #gets the card face property
        return self.__card_face
    def get_card_value(self):
        #gets the card value property
        return self.__card_value
    def set_card_value(self, new_card_value):
        #sets the card value property
        self.__card_value = new_card_value
    def get_card_position(self):
        #gets the card position property
        return self.__card_position
    def set_card_position(self, new_card_position):
        #sets the card position property
        self.__card_position = new_card_position
    def get_card_flipped(self):
        #gets the card flipped property
        return self.__card_flipped
    def set_card_flipped(self, new_card_flipped_boolean):
        #sets the card flipped property
        self.__card_flipped = new_card_flipped_boolean
    def get_card_name(self):
        #gets the card name property
        return self.__card_name
    
    #private methods
    def __find_card_face(self, index_number):
        # this method finds the name of the face texture based on the card's position
        list_of_names = ['card:ClubsA', 'card:DiamondsA', 'card:HeartsA', 'card:SpadesA', 'card:Clubs2', 'card:Diamonds2', 'card:Hearts2', 'card:Spades2', 'card:Clubs3', 'card:Diamonds3', 'card:Hearts3', 'card:Spades3', 'card:Clubs4', 'card:Diamonds4', 'card:Hearts4', 'card:Spades4', 'card:Clubs5', 'card:Diamonds5', 'card:Hearts5', 'card:Spades5', 'card:Clubs6', 'card:Diamonds6', 'card:Hearts6', 'card:Spades6', 'card:Clubs7', 'card:Diamonds7', 'card:Hearts7', 'card:Spades7', 'card:Clubs8', 'card:Diamonds8', 'card:Hearts8', 'card:Spades8', 'card:Clubs9', 'card:Diamonds9', 'card:Hearts9', 'card:Spades9', 'card:Clubs10', 'card:Diamonds10', 'card:Hearts10', 'card:Spades10', 'card:ClubsJ', 'card:DiamondsJ', 'card:HeartsJ', 'card:SpadesJ', 'card:ClubsQ', 'card:DiamondsQ', 'card:HeartsQ', 'card:SpadesQ', 'card:ClubsK', 'card:DiamondsK', 'card:HeartsK', 'card:SpadesK']
        
        self.__card_face = list_of_names[index_number]
    
    def __create_name(self):
        # This method when called creates a name for the card more user friendly
        
        # Remove 'Card:'
        finished_name = ''
        for letter in range(0, len(self.__card_face) - 5):
            finished_name = finished_name + str(self.__card_face[letter + 5])
        
        # Change last letter into 'x of y'
        if finished_name[len(finished_name) - 1] == 'A':
            self.__card_name = 'Ace of '
            for ace_recreate_name in range(0, len(finished_name) - 1):
                self.__card_name = self.__card_name + finished_name[ace_recreate_name]
        elif finished_name[len(finished_name) - 1] == 'J':
            self.__card_name = 'Jack of '
            for jack_recreate_name in range(0, len(finished_name) - 1):
                self.__card_name = self.__card_name + finished_name[jack_recreate_name]
        elif finished_name[len(finished_name) - 1] == 'Q':
            self.__card_name = 'Queen of '
            for queen_recreate_name in range(0, len(finished_name) - 1):
                self.__card_name = self.__card_name + finished_name[queen_recreate_name]
        elif finished_name[len(finished_name) - 1] == 'K':
            self.__card_name = 'King of '
            for king_recreate_name in range(0, len(finished_name) - 1):
                self.__card_name = self.__card_name + finished_name[king_recreate_name]
        elif finished_name[len(finished_name) - 1] == '0':
            self.__card_name = '10 of '
            for ten_recreate_name in range(0, len(finished_name) - 2):
                self.__card_name = self.__card_name + finished_name[ten_recreate_name]
        else:
            self.__card_name = finished_name[len(finished_name) - 1] + ' of '
            for number_recreate_name in range(0, len(finished_name) - 1):
                self.__card_name = self.__card_name + finished_name[number_recreate_name]
