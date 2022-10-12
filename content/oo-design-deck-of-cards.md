# Design a deck of cards

## Constraints and assumptions

* Is this a generic deck of cards for games like poker and black jack?
** Yes, design a generic deck then extend it to black jack
* Can we assume the deck has 52 cards (2-10, Jack, Queen, King, Ace) and 4 suits?
** Yes
* Can we assume inputs are valid or do we have to validate them?
** Assume they're valid

## Solution

```
from abc import ABCMeta, abstractmethod
from enum import Enum
import sys


class Suit(Enum):

    HEART = 0
    DIAMOND = 1
    CLUBS = 2
    SPADE = 3

class Card(metaclass=ABCMeta):

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.is_available = True

    @property
    @abstractmethod
    def value(self):
        pass

    @value.setter
    @abstractmethod
    def value(self, other):
        pass

class BlackJackCard(Card):

    def __init__(self, value, suit):
        super(BlackJackCard, self).__init__(value, suit)
```
