from typing import List
import heapq
from collections import defaultdict, deque



# class Node:
#     def __init__(self) -> None:
#         self.children = defaultdict(Node)
#         self.isWord = False

# class Trie:

#     def __init__(self):
#         self.root = Node()

#     def find(self, s: str) -> Node:
#         ptr = self.root # dict
#         for c in s:
#             if c not in ptr.children:
#                 return None
#             ptr = ptr.children[c] # ptr[c] is a Node
#         return ptr

#     def insert(self, word: str) -> None:
#         ptr = self.root
#         for c in word:
#             ptr = ptr.children[c]
#         ptr.isWord = True

#     def search(self, word: str) -> bool:
#         ptr = self.find(word)
#         if ptr == None:
#             return False
#         return ptr.isWord

#     def startsWith(self, prefix: str) -> bool:
#         ptr = self.find(prefix)
#         if ptr == None:
#             return False
#         return True

# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         m,n = len(board),len(board[0])
#         visited = [[False]*n for i in range(m)]
#         t = Trie()
#         maxWordLen = 0
#         for w in words:
#             t.insert(w)
#             if len(w) > maxWordLen:
#                 maxWordLen = len(w)
#         l = [None]*maxWordLen
#         lenl = 0
#         root = t.root
#         ans = set()

#         def bt(r,c,node):
#             nonlocal lenl
#             char = board[r][c]
#             if char not in node.children or lenl >= maxWordLen : # l condition?
#                 return
#             visited[r][c] = True
#             l[lenl] = char
#             node = node.children[char]
#             if node.isWord:
#                 ans.add("".join(l[:lenl+1]))
#             for roff,coff in [(1,0),(-1,0),(0,1),(0,-1)]:
#                 newr, newc = r+roff,c+coff
#                 if newr >= 0 and newr < m and newc >= 0 and newc < n and not visited[newr][newc]:
#                     lenl += 1
#                     bt(newr,newc,node)
#                     lenl -= 1

#             visited[r][c] = False

#         for i in range(m):
#             for j in range(n):
#                 bt(i,j,root)
#         return list(ans)

s = Solution()
assert s.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"])==["eat","oath"]
assert s.findWords([["a"]],["a"])==["a"]
assert s.findWords([["a","a"]],["aaa"])==[]