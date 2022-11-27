# Design an LRU cache

## Constraints and assumptions

* What are we caching?
** We are caching the results of web queries
* Can we assume inputs are valid or do we have to validate them?
** Assume they're valid
* Can we assume this fits memory?
** Yes

```
class Node(object):

    def __init__(self, results):
        self.results = results
        self.prev = None
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def move_to_front(self, node):  # ...
    def append_to_front(self, node):  # ...
    def remove_from_tail(self):  # ...
```
