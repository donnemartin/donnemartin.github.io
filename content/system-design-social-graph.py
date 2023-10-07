# -*- coding: utf-8 -*-
from collections import deque
from enum import Enum


class State(Enum):
    unvisited = 0
    visited = 1
