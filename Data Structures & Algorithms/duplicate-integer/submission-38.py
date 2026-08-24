class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = set()

        for i in nums:
            if i in prev:
                return True
            prev.add(i)
        return False        