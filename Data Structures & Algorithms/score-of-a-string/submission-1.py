class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in s:
            if i >= 0:
                res = ord(i) - ord(i-1)
        return res