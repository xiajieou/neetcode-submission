class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        for i in range(len(nums)):
            l = i - 1 
            if nums[i] == val:
                l, nums[i] = nums[i], l
        return nums