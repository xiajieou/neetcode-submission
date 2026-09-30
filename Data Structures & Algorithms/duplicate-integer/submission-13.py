class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = set()

        for num in nums:
            if num in count:
                return True
            num.add(num)
        return False