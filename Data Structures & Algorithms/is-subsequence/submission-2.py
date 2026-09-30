class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        countT = {}

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for i in s:
            if i not in countT:
                return False
        return True