# -*- coding: utf-8 -*-
from collections import deque
from enum import Enum


class State(Enum):
    unvisited = 0
    visited = 1


class Graph(object):

    def __init__(self):
        pass

    def bfs(self, source, dest):
        if source is None:
            return False
        queue = deque()
        queue.append(source)
        source.visit_state = State.visited
        while queue:
            node = queue.popleft()
            print(node)
            if dest is node:
                return True
            for adjacent_node in node.adj_nodes.values():
                if adjacent_node.visit_state == State.unvisited:
                    queue.append(adjacent_node)
                    adjacent_node.visit_state = State.visited
        return False


class Person(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.friend_ids = []


class LookupService(object):

    def __init__(self):
        self.lookup = {}  # key: person_id, value: person_server
