class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return true if any vals appears more than once else false
        nums_set = set()

        for element in nums:
            if element in nums_set:
                return True
            nums_set.add(element)
        return False