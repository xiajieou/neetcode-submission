class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_set = set()

        for i in nums:
            my_set.add(i)
        
        

        return list(my_set)