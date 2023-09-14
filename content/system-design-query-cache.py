# -*- coding: utf-8 -*-


class QueryApi(object):

    def __init__(self, memory_cache, reverse_index_cluster):
        self.memory_cache = memory_cache
        self.reverse_index_cluster = reverse_index_cluster

    def parse_query(self, query):
        """Remove markup, break text into terms, deal with typos,
        normalize capitalization, convert to use boolean operations.
        """
        ...

    def process_query(self, query):
        query = self.parse_query(query)
        results = self.memory_cache.get(query)
        if results is None:
            results = self.reverse_index_cluster.process_search(query)
            self.memory_cache.set(query, results)
        return results


class Node(object):

    def __init__(self, query, results):
        self.query = query
        self.results = results


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def move_to_front(self, node):
        ...

    def append_to_front(self, node):
        ...

    def remove_from_tail(self):
        ...
