from Deck import *


def main():
  # Create new deck
  deck = Deck()
  # Shuffle deck of cards
  deck.shuffle()

  # Draw a card to workout
  print(deck.draw_card())
  print(deck.draw_card())

  # Finish workout
  deck.complete_workout()


main()
