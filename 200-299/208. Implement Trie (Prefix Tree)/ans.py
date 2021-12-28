from typing import List
import heapq
from collections import defaultdict, deque

class Node:
    def __init__(self) -> None:
        self.children = defaultdict(Node)
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = Node()

    def find(self, s: str) -> Node:
        ptr = self.root # dict
        for c in s:
            if c not in ptr.children:
                return None
            ptr = ptr.children[c] # ptr[c] is a Node
        return ptr

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            ptr = ptr.children[c]
        ptr.isWord = True

    def search(self, word: str) -> bool:
        ptr = self.find(word)
        if ptr == None:
            return False
        return ptr.isWord

    def startsWith(self, prefix: str) -> bool:
        ptr = self.find(prefix)
        if ptr == None:
            return False
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "hey"
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith("he")
param_4 = obj.startsWith("eh")
print(param_2,param_3,param_4)