class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for s in range(len(strs[0])):
            for c in s:
                if strs[0][c] == len(s) or s[c] != strs[0][c]:
                    return res
            res += strs[0][c]
        return res