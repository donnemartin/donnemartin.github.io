# Design a hash map

## Constraints and assumptions

* For simplicity, are the keys integers only?
** Yes
* For collision resolution, can we use chaining?
** Yes
* Do we have to worry about load factors?
** No
* Can we assume inputs are valid or do we have to validate them?
** Assume they're valid
* Can we assume this fits memory?
** Yes

```
class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
```