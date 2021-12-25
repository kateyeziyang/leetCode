from typing import List
from collections import defaultdict, deque

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0
        while i<len(words):
            # start of a line
            wordWidth = len(words[i])
            numWords = 1
            for j in range(i+1,len(words)):
                if wordWidth+len(words[j])+numWords <= maxWidth:
                    numWords += 1
                    wordWidth += len(words[j])
                else:
                    break
            if i+numWords == len(words):
                line = words[i]
                for k in range(1,numWords):
                    line += " "+words[i+k]
                line += " "*(maxWidth-len(line))
                ans.append(line)
                break
            line = words[i]
            if numWords == 1:
                line += " "*(maxWidth-len(words[i]))
                i += 1
                ans.append(line)
                continue
            numSpaces = maxWidth-wordWidth
            baseSpaces, numExtraSpaces = numSpaces//(numWords-1), numSpaces%(numWords-1)
            for k in range(1,numExtraSpaces+1):
                line += " "*(baseSpaces+1)+words[i+k]
            for k in range(numExtraSpaces+1,numWords):
                line += " "*baseSpaces+words[i+k]
            ans.append(line)
            i += numWords
        return ans

s = Solution()
print(s.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))

print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], maxWidth = 16))

print(s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20))

"""
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

https://leetcode.com/problems/text-justification/discuss/24891/Concise-python-solution-10-lines.
def fullJustify(self, words, maxWidth):
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i%(len(cur)-1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(maxWidth)]
Do you really can use ljust() in an interview?? Actually doesn't matter so much

time complexity: O(n)
space: O(maxwidth) constant?
"""

"""
technically I think the hard point is time
"""