class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        count = {}
        for i in s:
            if i not in s:
                my_dict[i] = 0
            my_dict[i] += 1 
        for i in t:
            if i not in t:
                count[i] = 0
            count[i] += 1
        if my_dict == count:
            return True
        return False