class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s) - 1):
            sum = abs(ord(i) + ord(i-1))
        return sum