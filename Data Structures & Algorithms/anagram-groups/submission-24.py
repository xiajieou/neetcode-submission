class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # so i have to group all anagrams togehter into a sublist and return them in any order

        # we can create a count variable that has a length of 26 0 and we can append 1 value for the corresponding letter if it is anagram itshould have the same letter and then we can append it to the hash map we can make the hashmap a default dict so the edge case of a empty hashmap wouldnt affect us and we can make the list a tuple so we cant use list as keys in python

        res = defaultdict(list)

        for element in strs:
            count = [0] * 26
            for char in element:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(element)
        return list(res.values())

        

