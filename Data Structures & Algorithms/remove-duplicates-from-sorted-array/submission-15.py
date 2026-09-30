class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0

        for r in range(0, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r-1]
                l += 1
        return l