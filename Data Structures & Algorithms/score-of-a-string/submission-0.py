class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in s:
            res = ord(i) - ord(i+1)
        return res