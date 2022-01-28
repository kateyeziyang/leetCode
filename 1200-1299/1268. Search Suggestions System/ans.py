from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# binary search... hey... how can I come up with this idea?
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        for i in range(len(searchWord)):
            idx = bisect_left(products,searchWord[:i+1])
            cur = []
            for str in products[idx:idx+3]:
                if str.startswith(searchWord[:i+1]):
                    cur.append(str)
            ans.append(cur)
        return ans

# why not use heap!!!
# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         products.sort(reverse=True)
#         trie = {}
#         for word in products:
#             p = trie
#             for c in word:
#                 p = p.setdefault(c,{})
#             p["#"] = True
#         p = trie
#         ans = []
#         for i,c in enumerate(searchWord):
#             if c not in p:
#                 for _ in range(len(searchWord)-len(ans)):
#                     ans.append([])
#                 return ans
#             cur = []
#             p = p[c]
#             st = deque([[p,list(searchWord[:i+1])]])
#             count = 0
#             while st and count<3:
#                 node,buf = st.pop()
#                 if "#" in node:
#                     cur.append("".join(buf))
#                     count += 1
#                 for nb in node:
#                     if nb != "#":
#                         st.append([node[nb],buf+[nb]])
#             ans.append(cur)
#         return ans

s = Solution()
print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse"))