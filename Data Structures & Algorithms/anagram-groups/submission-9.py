class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in range(len(strs)):
            count = [0] * 26
            for s in strs:
                count[ord(s) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res