class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {')' : '(', '}' : '{', ']' : '['}
        final_array = []

        for i in s:
            if i in openToClose:
                if final_array and final_array[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False

            else:
                final_array.append(i)
        return True if not stack else False