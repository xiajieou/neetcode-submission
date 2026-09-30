class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = []
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                k+=1
                r.append(i)
        return k