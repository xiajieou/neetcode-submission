class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # so i have to group all anagrams togehter into a sublist and return them in any order

        # we can create a count variable that has a length of 26 0 and we can append 1 value for the corresponding letter if it is anagram itshould have the same letter and then we can append it to the hash map we can make the hashmap a default dict so the edge case of a empty hashmap wouldnt affect us and we can make the list a tuple so we cant use list as keys in python

        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

