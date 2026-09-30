class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if self.char_count(s) == self.char_count(t):
            return True
        return False
    def char_count(self,s):
        count = {}
        for i in s:
            if i not in s:
                count[i] = 0
            count[i] += 1 
        return count