class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return true if any vals appears more than once else false
        nums_set = set(nums)
        return len(nums) != len(nums_set)