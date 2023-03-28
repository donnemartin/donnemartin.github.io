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

    def is_ace(self):
        return True if self._value == 1 else False
