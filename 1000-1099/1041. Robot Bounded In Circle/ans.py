from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirMap = {"n":(0,1),"e":(1,0),"s":(0,-1),"w":(-1,0)}
        lMap = {"n":"w","e":"n","s":"e","w":"s"}
        rMap = {"n":"e","e":"s","s":"w","w":"n"}
        curLoc = [0,0]
        curDir = "n"
        for _ in range(4):
            for instr in instructions:
                if instr == "L":
                    curDir = lMap[curDir]
                elif instr == "R":
                    curDir = rMap[curDir]
                else:
                    curLoc[0] += dirMap[curDir][0]
                    curLoc[1] += dirMap[curDir][1]
            if curLoc[0] == 0 and curLoc[1] == 0:
                return True
        return False


s = Solution()
print(s.isRobotBounded(instructions = "GGLLGG"))
print(s.isRobotBounded(instructions = "GG"))
print(s.isRobotBounded(instructions = "GL"))