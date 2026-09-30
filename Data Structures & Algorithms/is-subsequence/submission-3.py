class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #s and t if s is subsequence of t true else false 
        set_t = set(t)

        for i in s:
            if i not in set_t:
                return False
        return True

        