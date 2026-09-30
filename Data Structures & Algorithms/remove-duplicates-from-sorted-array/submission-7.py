class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_set = set()

        for i in nums:
            if i not in my_set:
                 my_set.add(i)
        return list(my_set())