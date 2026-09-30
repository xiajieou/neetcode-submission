class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS= {}
        countT = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + CountS.get(s[i],0)
            countT[t[i]] = 1 + CountT.get(t[i],0)
        return countS == countT