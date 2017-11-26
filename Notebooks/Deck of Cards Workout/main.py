from Deck import *


def main():
  # Create new deck
  print("Welcome to the Deck of Cards Workout.\nLet's get a deck of cards to workout with...")
  deck = Deck()
  
  # Shuffle deck of cards
  print("\nNow let's shuffle it.")
  deck.shuffle()

  # Draw a card to workout
  print("\nOkay, let's warm up by drawing a few cards")
  print(deck.draw_card())
  print("\nLet's do another")
  print(deck.draw_card())
  print("\nLet's do another")
  print(deck.draw_card())

  # Finish workout
  print("\nOkay, now let's finish the workout!")
  deck.complete_workout()


main()
