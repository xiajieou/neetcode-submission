class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for s in strs[0]:
            for c in s:
                if i == len(s) or strs[0][i] != s[c]:
                    return res
            res += strs[0][i]
        return res 