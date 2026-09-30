class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for i in s:
            countS[i] = 1 + countS.get(s[i], 0)
        for i in t:
            countT[i] = 1 + countT.get(t[i], 0)

        for i in countS:
            if countS[i] not in countT:
                return False
        return True