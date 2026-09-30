class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in range(len(strs)):
            count = [0] * 26
            for c in strs:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(i)
        return res