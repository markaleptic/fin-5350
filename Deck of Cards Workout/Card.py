class Card(object):
  """
  Base class to represent a single card in a standard deck of cards
  """

  def __init__(self, value, face):
    self.__value = value
    self.__face = face

  def face(self):
    return self.__face

  def value(self):
    return self.__value

  def color(self):    pass
  def suit(self):     pass


class Red(Card):
  """
  Inherited class from Card to represent a card that is red
  """
  def __init__(self, value, face):
    super().__init__(value, face)
    self.__color = "Red"

  def color(self):
    return self.__color

  def suit(self):  pass


class Black(Card):
  """
  Inherited class from Card to represent a card that is black
  """
  def __init__(self, value, face):
    super().__init__(value, face)
    self.__color = "Black"
    
  def color(self):
    return self.__color
    
  def suit(self):  pass


class Diamonds(Red):
  """
  Inherited class from Red to represent a card with a Diamonds suit
  """
  def __init__(self, value, face):
    super().__init__(value, face)
    self.__suit = "Diamonds"

  def suit(self):
    return self.__suit


class Hearts(Red):
  """
  Inherited class from Red to represent a card with a Hearts suit
  """
  def __init__(self, value, face):
    super().__init__(value, face)
    self.__suit = "Hearts"

  def suit(self):
    return self.__suit

 
class Clubs(Black):
  """
  Inherited class from Black to represent a card with a Clubs suit
  """
  def __init__(self, value, face):
    super().__init__(value, face)
    self.__suit = "Clubs"

  def suit(self):
    return self.__suit


class Spades(Black):
  """
  Inherited class from Black to represent a card with a Spades suit
  """
  def __init__(self, value, face):
    super().__init__(value, face)
    self.__suit = "Spades"

  def suit(self):
    return self.__suit

class_list = [Clubs, Spades, Diamonds, Hearts]
