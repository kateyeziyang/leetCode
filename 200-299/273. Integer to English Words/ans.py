from typing import List
from collections import defaultdict, deque

"""
0~9,10~90,11~19
hundred 100,thousand 1000,million 1000 thousand,billion 1000 million

max 214 million
recursive, iterative

1. recursive
want to break in to 3-digit parts
in each 3-digit parts, use 0~100 hundreds
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        oneTo19 = ("One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
        "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen")
        tens = ("Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety")
        def helper(n):
            if n>= 1000000000:
                return helper(n//1000000000)+"Billion "+helper(n%1000000000)
            if n>= 1000000:
                return helper(n//1000000)+"Million "+helper(n%1000000)
            if n>= 1000:
                return helper(n//1000)+"Thousand "+helper(n%1000)
            # only n< 1000 are here
            words = ""
            if n >= 100:
                words += oneTo19[(n//100)-1]+" Hundred "
                n %= 100
            if n >= 20:
                words += tens[(n//10)-2]+" "
                if n%10:
                    words += oneTo19[(n%10)-1]+" "
            else:
                if n%20:
                    words += oneTo19[n-1]+" "
            return words
        ans = helper(num)
        if ans[len(ans)-1] == " ":
            ans = ans[:-1]
        return ans

s = Solution()
print(s.numberToWords(100))
print(s.numberToWords(1))
print(s.numberToWords(20))
print(s.numberToWords(123))
print(s.numberToWords(1234))
print(s.numberToWords(654321))
print(s.numberToWords(7654321))
print(s.numberToWords(987654321))
assert s.numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

"""
def numberToWords(self, num):
    to19 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve " \
           "Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    def words(n):
        if n < 20:
            return to19[n-1:n]
        if n < 100:
            return [tens[n//10-2]]+words(n%10)
        if n < 1000:
            return [to19[n//100-1]]+["Hundred"]+words(n%100)
        for p,w in enumerate(("Thousand","Million","Billion"),1):
            if n < 1000**(p+1):
                return words(n//1000**p)+[w]+words(n%1000**p)
    return " ".join(words(num)) or "Zero"
"""