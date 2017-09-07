import math

def main():
  lbound = 0
  ubound = 10000
  maxGuesses = math.ceil(math.log(ubound,2))
  guess = 0
  global tryCount
  tryCount = 1

  print("Welcome to the Number Guessing Game\nI will guess your number, between %d and %d in %d tries or less" % (lbound, ubound,maxGuesses))
  userNumber = input("Enter your number here (I promise I won't peak): ")
  
  while not isinstance(userNumber, int):
    print("Looks like there was an error with what you input! Please input a whole number.")
    userNumber = input("Enter your number here: ")
  
  guessNumber(guess, lbound, ubound)
  
def guessNumber(guess, lbound, ubound):
  global tryCount
  guess = (ubound - lbound) / 2
  if tryCount > 1:
    guess += lbound
  guess = int(guess)
  
  print("\nIs your number %d?" % guess)
  guessCorrect = raw_input("(y / n) ")
  
  while not (isinstance(guessCorrect, str) and len(guessCorrect) == 1) or (guessCorrect != 'n' and guessCorrect != 'y'):
    print("\nLooks like there was an error with your input! Please respond with a 'y' for yes and 'n' for no.")
    print("Is your number %d?" % guess)
    guessCorrect = raw_input("(y / n) ")
  
  
  if guessCorrect == "y":
    print("\nYour number is %d. It took me %d attempts to guess your number" % (guess, tryCount))
    print("Want to play again?")
    playAgain = raw_input("(y / n) ")
    
    while not isinstance(playAgain, str) and len(playAgain) == 1:
      print("\nLooks like there was an error with your input! Please respond with a 'y' for yes and 'n' for no.")
      print("Want to play again?")
      playAgain = raw_input("(y / n) ")
      
    if playAgain == 'y':
      print("\n")
      main()
    else:
      quit()
    
    return True
  elif guessCorrect == 'n':
    tryCount += 1
    
    higherOrLower = raw_input("\nIs your number higher or lower than my guess? \n(h / l) ")
    
    while not (isinstance(higherOrLower, str) and len(higherOrLower) == 1) or (higherOrLower != 'l' and higherOrLower != 'h'):
      print("\nLooks like there was an error with your input! Please respond with an 'h' for higher and 'l' for lower.")
      higherOrLower = raw_input("\nIs your number higher or lower than my guess? \n(h / l) ")
    
    if higherOrLower == 'h':
      lbound = guess
      guessNumber(guess, lbound, ubound)
    elif higherOrLower == 'l':
      ubound = guess
      guessNumber(guess, lbound, ubound)
    


main()