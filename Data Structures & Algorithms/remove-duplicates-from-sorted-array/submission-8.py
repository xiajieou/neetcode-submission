class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_set = set()

        for i in nums:
            if i not in my_set:
                 my_set.add(i)
        print(my_set())