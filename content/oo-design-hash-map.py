class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
