from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left
from random import randint
class RandomizedSet:

    def __init__(self):
        self.items = set()
        self.d = {}
        self.rd = {}

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        self.items.add(val)
        self.d[len(self.d)] = val
        self.rd[val] = len(self.rd)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.items:
            return False
        self.items.remove(val)
        self.d.pop(self.rd[val])
        self.rd.pop(val)
        return True

    def getRandom(self) -> int:
        idx = randint(0,len(self.items)-1)
        return self.d[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# index to val, 0-10 remove
# set to store index
class RandomizedSet:

    def __init__(self):
        self.i2v = {}
        self.v2i = {}

    def insert(self, val: int) -> bool:
        if val in self.v2i:
            return False
        self.v2i[val] = len(self.i2v)
        self.i2v[len(self.i2v)] = val
        return True

    def remove(self, val: int) -> bool:
        if val in self.v2i:
            i = self.v2i[val]
            if i == len(self.v2i):
                del self.i2v[i]
            else:
                self.i2v[i] = self.i2v[len(self.i2v)-1]
                self.v2i[self.i2v[i]] = i
                del self.i2v[len(self.i2v)-1]
            del self.v2i[val]
            return True
        return False

    def getRandom(self) -> int:
        randomIdx = random.randint(0, len(self.i2v)-1)
        return self.i2v[randomIdx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

s = RandomizedSet()
s.insert(1)
s.remove(2)
s.insert(2)
s.remove(1)
s.insert(2)
print(s.getRandom())