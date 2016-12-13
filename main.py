# Created by: Matthew Lourenco
# Created on: 12 Dec 2016
# This is the stub program of the 21 program using oop

import ui
import time
import console
from deck_of_cards import *

#global variables
money = 20
bet = 0
deck = None
computer_cards_flipped = False
bet_set = False

@ui.in_background

def reset_game():
    #resets the game
    for reset_animation in range(0, 4):
        view['reply_label'].text = view['reply_label'].text + '.'
        time.sleep(0.25)
    view['reply_label'].text = ''
    
    global deck
    deck = DeckOfCards()
    view['card1_imageview'].image = ui.Image(deck.get_card_back())
    view['card2_imageview'].image = ui.Image(deck.get_card_back())
    view['card3_imageview'].image = ui.Image(deck.get_card_back())
    view['card4_imageview'].image = ui.Image(deck.get_card_back())
    view['card5_imageview'].image = ui.Image(deck.get_card_back())
    view['card6_imageview'].image = ui.Image(deck.get_card_back())
    view['card6_imageview'].alpha = 0.5
    view['card6_instructions_label'].alpha = 1
    view['bet_textfield'].text = '5'
    global computer_cards_flipped
    computer_cards_flipped = False
    global bet_set
    bet_set = False
    
    if money < 5:
        view['bet_textfield'].text = str(money)
    
    deck.shuffle()

def restart_game_touch_up_inside(sender):
    # Restarts the game completely
    global money
    money = 20
    view['money_label'].text = ' Total Money: $20'
    view['reply_label'].text = 'Restarting'
    reset_game()

def check_bet():
    #checks the bet to see if it is valid
    global bet_set
    global bet
    
    if bet_set == True:
        return True
    elif view['bet_textfield'].text == '':
        view['reply_label'].text = "Please enter a bet before flipping the opponent's cards."
        return False
    else:
        try:
            if money < 5 and int(view['bet_textfield'].text) == money:
                bet = int(view['bet_textfield'].text)
                bet_set = True
                view['bet_label'].text = ' Bet = ' + str(bet)
                view['bet_textfield'].text = ''
                return True
            elif money < 5 and not int(view['bet_textfield'].text) == money:
                view['reply_label'].text = 'You must bet all of your money since you have less than 5 dollars.'
                return False
            elif int(view['bet_textfield'].text) > money or int(view['bet_textfield'].text) < 5:
                view['reply_label'].text = "Please enter a bet that is less than your total money but at least 5 dollars."
                return False
            else:
                bet = int(view['bet_textfield'].text)
                bet_set = True
                view['bet_label'].text = ' Bet = ' + str(bet)
                view['bet_textfield'].text = ''
                return True
        except:
            view['reply_label'].text = "Please enter a bet that is a whole number."
            return False

def choose_ace_value(player_card):
    #lets the player decide what value to give their ace
    if computer_cards_flipped:
        player_card.set_card_value(1)
        view['reply_label'].text = 'The value of ' + str(player_card.get_card_name()) + " is now 1 because you have already seen the opponent's cards"
    elif console.alert('ALERT', 'choose the value of your ace', '1', '11', hide_cancel_button = True) == 1:
        player_card.set_card_value(1)
        view['reply_label'].text = 'The value of ' + str(player_card.get_card_name()) + ' is now 1.'
    else:
        player_card.set_card_value(11)
        view['reply_label'].text = 'The value of ' + str(player_card.get_card_name()) + ' is now 11.'

@ui.in_background

def flip_card_touch_up_inside(sender):
    #Flips card to reveal card face
    global computer_cards_flipped
    global money
    if sender.name == 'card1_button' and not deck.get_computer_cards()[0].get_card_flipped() and check_bet():
        view['card1_imageview'].image = ui.Image(deck.get_computer_cards()[0].get_card_face())
        deck.get_computer_cards()[0].set_card_flipped(True)
        computer_cards_flipped = True
    elif sender.name == 'card2_button' and not deck.get_computer_cards()[1].get_card_flipped() and check_bet():
        view['card2_imageview'].image = ui.Image(deck.get_computer_cards()[1].get_card_face())
        deck.get_computer_cards()[1].set_card_flipped(True)
        computer_cards_flipped = True
    elif sender.name == 'card3_button' and not deck.get_computer_cards()[2].get_card_flipped() and check_bet():
        view['card3_imageview'].image = ui.Image(deck.get_computer_cards()[2].get_card_face())
        deck.get_computer_cards()[2].set_card_flipped(True)
        computer_cards_flipped = True
    elif sender.name == 'card4_button' and not deck.get_player_cards()[0].get_card_flipped():
        view['card4_imageview'].image = ui.Image(deck.get_player_cards()[0].get_card_face())
        deck.get_player_cards()[0].set_card_flipped(True)
        if deck.get_player_cards()[0].get_card_value() == 1:
            choose_ace_value(deck.get_player_cards()[0])
    elif sender.name == 'card5_button' and not deck.get_player_cards()[1].get_card_flipped():
        view['card5_imageview'].image = ui.Image(deck.get_player_cards()[1].get_card_face())
        deck.get_player_cards()[1].set_card_flipped(True)
        if deck.get_player_cards()[1].get_card_value() == 1:
            choose_ace_value(deck.get_player_cards()[1])
    elif sender.name == 'card6_button' and not deck.get_player_cards()[2].get_card_flipped() and not computer_cards_flipped:
        view['card6_imageview'].image = ui.Image(deck.get_player_cards()[2].get_card_face())
        deck.get_player_cards()[2].set_card_flipped(True)
        view['card6_imageview'].alpha = 1
        view['card6_instructions_label'].alpha = 0
        if deck.get_player_cards()[2].get_card_value() == 1:
            choose_ace_value(deck.get_player_cards()[2])
    
    # checks if first 5 cards are flipped then finds the winner and resets the game
    if deck.get_computer_cards()[0].get_card_flipped() and deck.get_computer_cards()[1].get_card_flipped() and deck.get_computer_cards()[2].get_card_flipped() and deck.get_player_cards()[0].get_card_flipped() and deck.get_player_cards()[1].get_card_flipped():
        if find_winner():
            money = money + bet
            view['money_label'].text = ' Total Money: $' + str(money)
            view['bet_label'].text = ' Bet = '
            time.sleep(1)
            reset_game()
        else:
            money = int(money) - int(bet)
            view['money_label'].text = ' Total Money: $' + str(money)
            view['bet_label'].text = ' Bet = '
            time.sleep(1)
            if money == 0:
                view['reply_label'].text = view['reply_label'].text + "\nYou're out of money! Press restart to play again!"
            else:
                reset_game()

def find_winner():
    # this method finds the winner
    #find each total
    computer_cards_total = 0
    player_cards_total = 0
    
    for computer_total_index in deck.get_computer_cards():
        computer_cards_total = computer_cards_total + computer_total_index.get_card_value()
    
    #if the computer cards are below 12 and the computer posseses an ace the ace will be worth 11
    for computer_ace_check in deck.get_computer_cards():
        if computer_ace_check.get_card_value() == 1 and computer_cards_total < 12:
            computer_cards_total = computer_cards_total + 10
    
    if deck.get_player_cards()[2].get_card_flipped():
        for player_total_index in deck.get_player_cards():
            player_cards_total = player_cards_total + player_total_index.get_card_value()
    else:
        player_cards_total = deck.get_player_cards()[0].get_card_value() + deck.get_player_cards()[1].get_card_value()
    
    #decide the winner by comparing the totals
    if player_cards_total == computer_cards_total:
        view['reply_label'].text = "You lost. \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
        return False
    
    elif player_cards_total > 21 and computer_cards_total > 21:
        view['reply_label'].text = "You lost. \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
        return False
    
    elif player_cards_total > computer_cards_total and player_cards_total < 22:
        view['reply_label'].text = "You Won! \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
        return True
    
    elif computer_cards_total < 22:
        view['reply_label'].text = "You lost. \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
        return False
    
    else:
        view['reply_label'].text = "You Won! \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
        return True

view = ui.load_view()
view.present('fullscreen', hide_title_bar = True)

#these lines do the first time setup on startup.
view['bet_explanation_label'].text = 'Bet Rules:\n-> Bets must be whole numbers.\n-> Bets must not be more than your total money but at least $5 unless your total money is $4 or less.'
view['money_label'].text = ' Total Money: $20'
reset_game()
