# collections module
# 1. Counter
# 2. defaultdict
# 3. OrderedDict
# 4. deque
# 5. ChainMap
# 6. namedtuple

# Counter: subclass of dictionary object
# takes an ileterable as an argument
# returns a dictionary with key as element and value as the number of times that element exists in the iterable

from collections import Counter,defaultdict, OrderedDict

# using Counter() function without arguments
cnt = Counter()

print(cnt)

mylist = [1,2,3,4,1,2,6,7,3,8,1]

name_list  = ['James','Kering','Alloyes','James']

print(Counter(mylist))
print(Counter(name_list))

# dictionary
print(Counter({1:3,2:4}))

# other functions in Counter include
# 1. element()
# 2. most_common()
# 3. substract()

cnt = Counter({1:3,2:4})
print(list(cnt.elements()))

# most common
cnt = Counter(mylist)
print(cnt.most_common())

# deduct
cnt = Counter({1:3,2:4})
deduct = {1:1,2:2}
cnt.subtract(deduct)
print(cnt)

# defaultdic works exactly like a python dictionary except for it does not throw KeyError when you try to access a non-existent key
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2

# trying to get four that is not in the dictionary
print(nums['four'])

count = defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for names in names_list:
    count[names] +=1
print(count)

# OrderedDict
# dictionary where keys nmaintain the order in which they are inserted
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)

from collections import deque

# is a list optimized for inserting and removing items
deq_list = ['a','b','c']
deq = deque(deq_list)
print(deq)

# add element to the right
deq.append('d')

# add element to the left
deq.appendleft('e')

print(deq)

deq.pop()
deq.popleft()

print(deq)

# clear all items on the list
deq.clear()

print(deq)

# ChainMap(): combine several dictionaries or mapping
from collections import ChainMap

dict1 = { 'a': 1, 'b': 2}
dict2 = { 'c': 3, 'd': 4}

chain_map = ChainMap(dict1,dict2)
print(chain_map.maps)
dict2['d'] = 5

print(chain_map['d'])

# getting keys and values from chainmap
print(list(chain_map.keys()))
print(list(chain_map.values()))

from collections import namedtuple

Student = namedtuple('Student','fname, lname, age')
s1 = Student('John','Clarke','13')
print(s1)

# creating a namedtuple using _make
