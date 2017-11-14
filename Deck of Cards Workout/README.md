# Deck of Cards Workout Submission
This is the submission for the Deck of Cards Workout assignment. The deck of cards is modeled after a standard 52-card deck:

![Standard 52-Card Deck](https://github.com/markaleptic/fin-5350/blob/master/Deck%20of%20Cards%20Workout/stdDeck.PNG)

Given the parameters of the assignment, Ace is high and represents 11 only and the other face cards represent 10. The workout goes like this:
1. Shuffle a standard deck
2. Draw a card from the top of the deck. The value of the card tells you the number of exercises you do, while the color tells you which exercise.
    - Black = Pushups
    - Red = Burpees or Squat Thrusts
    - Ex. 7 of spades = 7 pushups, Ace of Hearts = 11 Burpees
3. Discard and draw again.
4. Repeat until no cards remain


## Data Model
- Card
  - Red
    - Hearts
    - Diamonds
  - Black
    - Clubs
    - Spades
- Deck


Each card is constructed from a Card base class, which encapsulates a face and workout value. Each card will be 
an instance of Red or Black, which enacapsulates card color. These inherit from the Card base class. The suit 
classes inherit from their requesite color class and, thus, encapsulate the suit of the card.

A seperate Deck class creates the instances of the cards and loads each into a list. Users can create a deck, 
shuffle the cards, draw a card (no replacement), or complete the workout in one-go.



## Homework Description
>In this problem you will write object-oriented code to simulate the ***Deck of Cards Workout*** from Ross
>Enamait's book *Never Gymless*.
>
>The details are given as follows from Enamait's book:
>
>This workout requires a standard deck of 52 playing cards. Each red card (diamonds and hearts) will require a set
>of burpees. Each black card (spades and clubs) will require a set of pushups.
>
>To perform the workout, start with a fully shuffled deck of cards. All face cards (Jacks, Queen, and King) have a
>value of 10. Aces have a value of 11. Number cards will be face value (ex. 7 of spades = 7 pushups). Do not use
>Joker cards for this problem.
>
>Each card requires a set of pushups or burpees, depending on the color of the card. Strive to work through the
>entire deck as fast as possible. If burpees become too difficult, switch to squat thrusts. 
>
>**Deck of Cards**
>
>- Burpees for every red card
>- Pushups for every black card
>
>You will need to create classes with the appropriate data members and methods to simulate this process. You will
>need classes for the deck of cards, for the different suites of cards (diamonds, hearts, spades, clubs). You
>will need methods for drawing from the deck without replacement (*hint:* represent the deck as a list of
>cards, and use a pseudo-random number to sample randomly and the *pop* method to pull it from the list). You will
>also want a method that can randomly shuffle the deck, etc. Think carefully about this and plan it out before
>you begin to write any code.
