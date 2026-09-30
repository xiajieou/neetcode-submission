class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if char_count(s) == char_count(t):
            return True
        return False
    def char_count(s):
        count = {}
        for i in s:
            if i not in s:
                count[i] = 0
            count[i] += 1 
        return count