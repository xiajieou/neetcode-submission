class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.char_count(s) == self.char_count(t)

    def char_count(self,s):
        count = {}
        for i in s:
            if i not in count:
                count[i] = 0
            count[i] += 1
        return count