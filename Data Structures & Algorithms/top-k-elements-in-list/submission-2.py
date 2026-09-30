class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k = 0 
        count = 0 

        for i in nums:
            if count == 0:
                k = i
            count = count + (1 if count == 0 else -1)
        return list(k)