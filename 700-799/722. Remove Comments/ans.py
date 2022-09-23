from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        def appendToResult():
            nonlocal addNewLine
            print(addNewLine, line[prev:i])
            if i-prev:
                if not result or addNewLine:
                    result.append(line[prev:i])
                    addNewLine = False
                else:
                    result[-1] += line[prev:i]
        isMultiCommentOn = False
        result = []
        addNewLine = False

        for line in source:
            i = 0
            prev = 0
            if not line: continue
            while i < len(line):
                if isMultiCommentOn:
                    idx = line.find('*/', i)
                    if idx == -1:
                        break
                    i = idx + 2
                    isMultiCommentOn = False
                    prev = i
                    continue
                token = line[i:i+2]
                if token == '/*':
                    isMultiCommentOn = True
                    appendToResult()
                    i += 2
                    continue
                if token == '//':
                    appendToResult()
                    addNewLine = True
                    break
                i += 1
            else:
                appendToResult()
                addNewLine = True
        return result

s = Solution()
# s.removeComments(["main() { ", "  int a = 1; /* Its comments here ", "", "  ", "  */ return 0;", "} "])
s.removeComments(["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"])