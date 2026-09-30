class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        count = {}
        for i in s:
            if i not in s:
                my_dict[i] = 0
            my_dict[i] += 1 
        for j in t:
            if j not in t:
                count[j] = 0
            count[j] += 1
        if my_dict == count:
            return True
        return False