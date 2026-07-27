class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        """
        u
        i = 9 9 9 
        o = 1 0 0 0 

        add by 1 
        p

        i

        """

        if not digits:
            return [1]


        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]

        #o(n) time


        #o(n) space

