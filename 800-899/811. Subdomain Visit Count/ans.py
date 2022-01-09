from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

# it's easier not to use a trie, why I use a trie?

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        trie = {}
        for pair in cpdomains:
            p = trie
            tmp = pair.split(" ")
            count = int(tmp[0])
            domains = tmp[1].split(".")
            for dom in domains[::-1]:
                p = p.setdefault(dom,{"#":0})
                p["#"] += count
        ans = []
        p = trie
        q = deque([[trie,[]]])
        while q:
            node,stringBuffer = q.popleft()
            for k,v in node.items():
                if k=="#": continue
                newStringBuffer = stringBuffer + [k]
                q.append([v,newStringBuffer])
                ans.append(str(node[k]["#"])+" "+".".join(newStringBuffer[::-1]))
        return ans

s = Solution()
print(s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))