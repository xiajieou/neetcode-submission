class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        updated = []
        for i in range(len(nums)):
            if nums[i] != val:
                updated.append(nums[i])
        return updated