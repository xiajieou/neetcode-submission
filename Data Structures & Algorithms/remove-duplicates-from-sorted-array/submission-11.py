class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[k] = nums[r]
        return k