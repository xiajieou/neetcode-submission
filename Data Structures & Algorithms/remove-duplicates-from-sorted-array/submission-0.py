class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_set = set()

        for i in nums:
            my_set.add(i)
        
        count = 0

        for i in my_set:
            count += 1
        return count 