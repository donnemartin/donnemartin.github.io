class Node(object):

    def __init__(self, results):
        self.results = results
        self.next = next


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def move_to_front(self, node):
        pass
