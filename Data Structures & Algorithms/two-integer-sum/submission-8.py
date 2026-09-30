class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                return [i, hashmap[target-nums[i]]]
            
            


