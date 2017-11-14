from random import shuffle
from Card import *


class Deck(object):
  """
  Class to hold and operate on a standard deck of cards
  """

  standard_deck = {2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 10 : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11 }

  def __init__(self):
    self.__arr = [None]*52
    iter = 0
    for face in Deck.standard_deck:
      for suit in class_list:
        card = suit(Deck.standard_deck[face], face)
        self.__arr[iter] = card
        iter += 1

  def cards_in_deck(self):
    return len(self.__arr)

  def shuffle(self):
    if self.cards_in_deck() != 0:
      shuffle(self.__arr)
    else:
      print("No cards remaining! Create a new deck to start another workout")


  def draw_card(self):
    if self.cards_in_deck() != 0:
      card = self.__arr.pop()
      workout = ('burpees', 'pushups')[card.color() == 'Black'] 
      str1 = 'You pulled the ' + card.color() + ' ' + str(card.face()) + ' of '+ card.suit()
      str2 = 'You must do ' + str(card.value()) + ' ' + str(workout)
      rStr = str1.ljust(35) + '\t' + str2.ljust(25)
      return rStr
    else:
      return "No cards remaining! Create a new deck to start another workout"
  
  def complete_workout(self):
    while(self.cards_in_deck() != 0):
      print(self.draw_card())
    print('Congratulations! You completed the Deck of Cards Workout')
