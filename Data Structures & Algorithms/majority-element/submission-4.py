class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        for i in nums:
            count = i 
            count = count + (1 if count == i else - 1)
        return count 
