from abc import ABCMeta, abstractmethod
from enum import Enum
import sys


class Suit(Enum):

    HEART = 0
    DIAMOND = 1
    CLUBS = 2
    SPADE = 3
