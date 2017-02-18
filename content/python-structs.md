Title: Python for Data Part 1: Data Structures
Date: 2016-09-24
Summary: Tuples, lists, dicts, and sets, with a focus on usage for data analysis.
Tags: Python
CoverImage: http://i.imgur.com/CLt4zpV.png
Thumbnail: http://i.imgur.com/0MvP2Ft.png

# Data Structures

* tuple
* list
* dict
* set

## tuple

A tuple is a one dimensional, fixed-length, immutable sequence.

Create a tuple:

```python
tup = (1, 2, 3)
tup
```

`(1, 2, 3)`

Convert to a tuple:

```python
list_1 = [1, 2, 3]
type(tuple(list_1))
```

`tuple`

Create a nested tuple:

```python
nested_tup = ([1, 2, 3], (4, 5))
nested_tup
```

`([1, 2, 3], (4, 5))`

Access a tuple's elements by index O(1):

```python
nested_tup[0]
```

`[1, 2, 3]`

Although tuples are immutable, their contents can contain mutable objects.

Modify a tuple's contents:

```python
nested_tup[0].append(4)
nested_tup[0]
```

`[1, 2, 3, 4]`

Concatenate tuples by creating a new tuple and copying objects:

```python
(1, 3, 2) + (4, 5, 6)
```

`(1, 3, 2, 4, 5, 6)`

Multiply tuples to copy references to objects (objects themselves are not copied):

```python
('foo', 'bar') * 2
```

`('foo', 'bar', 'foo', 'bar')`

Unpack tuples:

```python
a, b = nested_tup
a, b
```

`([1, 2, 3, 4], (4, 5))`

Unpack nested tuples:

```python
(a, b, c, d), (e, f) = nested_tup
a, b, c, d, e, f
```

`(1, 2, 3, 4, 4, 5)`

A common use of variable unpacking is when iterating over sequences of tuples or lists:

```python
seq = [( 1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print(a, b, c)
```

`(1, 2, 3)`

`(4, 5, 6)`

`(7, 8, 9)`

## list

A list is a one dimensional, variable-length, mutable sequence.

Create a list:

```python
list_1 = [1, 2, 3]
list_1
```

`[1, 2, 3]`

Convert to a list:

```python
type(list(tup))
```

`list`

Create a nested list:

```python
nested_list = [(1, 2, 3), [4, 5]]
nested_list
```

`[(1, 2, 3), [4, 5]]`

Access a list's elements by index O(1):

```python
nested_list[1]
```

`[4, 5]`

Append an element to a list O(1):

```python
nested_list.append(6)
nested_list
```

`[(1, 2, 3), [4, 5], 6]`

Insert an element to a list at a specific index (note that insert is expensive as it has to shift subsequent elements O(n)):

```python
nested_list.insert(0, 'start')
nested_list
```

`['start', (1, 2, 3), [4, 5], 6]`

Pop is expensive as it has to shift subsequent elements O(n).  The operation is O(1) if pop is used for the last element.

Remove and return an element from a specified index:

```python
nested_list.pop(0)
nested_list
```

`[(1, 2, 3), [4, 5], 6]`

Locates the first such value and remove it O(n):

```python
nested_list.remove((1, 2, 3))
nested_list
```

`[[4, 5], 6]`

Check if a list contains a value O(n):

```python
6 in nested_list
```

`True`

Concatenate lists by creating a new list and copying objects:

```python
[1, 3, 2] + [4, 5, 6]
```

`[1, 3, 2, 4, 5, 6]`

Extend a list by appending elements (faster than concatenating lists, as it does not have to create a new list):

```python
nested_list.extend([7, 8, 9])
nested_list
```

`[[4, 5], 6, 7, 8, 9]`

## dict

A dict is also known as a hash map or associative array.  A dict is a mutable collection of key-value pairs.

Note: Big O complexities are listed as average case, with most worst case complexities being O(n).

Create a dict:

```python
dict_1 = { 'a' : 'foo', 'b' : [0, 1, 2, 3] }
dict_1
```

`{'a': 'foo', 'b': [0, 1, 2, 3]}`

Access a dict's elements by index O(1)

```python
dict_1['b']
```

`[0, 1, 2, 3]`

Insert or set a dict's elements by index O(1):

```python
dict_1[5] = 'bar'
dict_1
```

`{5: 'bar', 'a': 'foo', 'b': [0, 1, 2, 3]}`

Check if a dict contains a key O(1):

```python
5 in dict_1
```

`True`

Delete a value from a dict O(1):

```python
dict_2 = dict(dict_1)
del dict_2[5]
dict_2
```

`{'a': 'foo', 'b': [0, 1, 2, 3]}`

Remove and return an element from a specified index O(1):

```python
value = dict_2.pop('b')
print(value)
print(dict_2)
```

`[0, 1, 2, 3]`
`{'a': 'foo'}`

Get or pop can be called with a default value if the key is not found.  By default, get() will return None and pop() will throw an exception if the key is not found.

```python
value = dict_1.get('z', 0)
value
```

`0`

Return a default value if the key is not found:

```python
print(dict_1.setdefault('b', None))
print(dict_1.setdefault('z', None))
```

`[0, 1, 2, 3]`
`None`

By contrast to setdefault(), defaultdict lets you specify the default when the container is initialized, which works well if the default is appropriate for all keys:

```python
from collections import defaultdict

seq = ['foo', 'bar', 'baz']
first_letter = defaultdict(list)
for elem in seq:
    first_letter[elem[0]].append(elem)
first_letter
```

`defaultdict(<type 'list'>, {'b': ['bar', 'baz'], 'f': ['foo']})`

dict keys must be "hashable", i.e. they must be immutable objects like scalars (int, float, string) or tuples whose objects are all immutable.  Lists are mutable and therefore are not hashable, although you can convert the list portion to a tuple as a quick fix.

```python
print(hash('string'))
print(hash((1, 2, (3, 4))))
```

`-9167918882415130555`
`-2725224101759650258`

Get the list of keys in no particular order (although keys() outputs the keys in the same order).  In Python 3, keys() returns an iterator instead of a list.

```python
dict_1.keys()
```

`['a', 'b', 5, 'z']`

Get the list of values in no particular order (although values() outputs the keys in the same order).  In Python 3, keys() returns an iterator instead of a list.

```python
dict_1.values()
```

`['foo', [0, 1, 2, 3], 'bar', None]`

Iterate through a dictionary's keys and values:

```python
for key, value in dict_1.items():
    print key, value
```

`a foo`

`b [0, 1, 2, 3]`

`5 bar`

`z None`

Merge one dict into another:

```python
dict_1.update({'e' : 'elephant', 'f' : 'fish'})
dict_1
```

`{5: 'bar',
 'a': 'foo',
 'b': [0, 1, 2, 3],
 'e': 'elephant',
 'f': 'fish',
 'z': None}`

Pair up two sequences element-wise in a dict:

```python
mapping = dict(zip(range(7), reversed(range(7))))
mapping
```

`{0: 6, 1: 5, 2: 4, 3: 3, 4: 2, 5: 1, 6: 0}`

## set

A set is an unordered sequence of unique elements.

Create a set:

```python
set_1 = set([0, 1, 2, 3, 4, 5])
set_1
```

`{0, 1, 2, 3, 4, 5}`

```python
set_2 = {1, 2, 3, 5, 8, 13}
set_2
```

`{1, 2, 3, 5, 8, 13}`

Sets support set operations like union, intersection, difference, and symmetric difference.

Union O(len(set_1) + len(set_2)):

```python
set_1 | set_2
```

`{0, 1, 2, 3, 4, 5, 8, 13}`

Intersection O(min(len(set_1), len(set_2)):

```python
set_1 & set_2
```

`{1, 2, 3, 5}`

Difference O(len(set_1)):

```python
set_1 - set_2
```

`{0, 4}`

Symmetric Difference O(len(set_1)):

```python
set_1 ^ set_2
```

`{0, 4, 8, 13}`

Subset O(len(set_3)):

```python
set_3 = {1, 2, 3}
set_3.issubset(set_2)
```

`True`

Superset O(len(set_3)):

```python
set_2.issuperset(set_3)
```

`True`

Equal O(min(len(set_1), len(set_2)):

```python
{1, 2, 3} == {3, 2, 1}
```

`True`
