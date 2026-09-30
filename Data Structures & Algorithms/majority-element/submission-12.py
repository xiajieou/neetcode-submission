class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        appear_most = 0
        freq = 0
        for i in nums:
            if appear_most != i:
                freq -= 1
            if appear_most == 0:
                appear_most = i
                freq += 1
            
        return appear_most