class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        for num in nums:
            if num in my_set:
                my_set.add(num)
            else:
                return False
