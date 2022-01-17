from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort(reverse=True)
        trie = {}
        for prod in products:
            ptr = trie
            for c in prod:
                ptr = ptr.setdefault(c,{})
            ptr["#"] = True
        ans = []
        ptr = trie
        strcache = []
        for c in searchWord:
            if c in ptr:
                ptr = ptr[c]
                strcache.append(c)
                count = 0
                suggestions = []
                st = deque([[ptr,strcache]])
                while st:
                    node,buf = st.pop()
                    if "#" in node:
                        count += 1
                        suggestions.append("".join(buf))
                        if count==3:
                            break
                    for nb in node:
                        if nb != "#":
                            st.append([node[nb],buf+[nb]])
                ans.append(suggestions)
            else:
                for _ in range(len(searchWord)-len(ans)):
                    ans.append([])
                break
        return ans

s = Solution()
print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse"))