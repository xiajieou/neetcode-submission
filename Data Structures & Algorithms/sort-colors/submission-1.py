class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0,0,0]

        for n in nums:
            count[n] += 1


        i = 0

        for n in range(len(nums)):
            for j in range(count[n]):
                nums[i] = n 
                i += 1
        return nums
        