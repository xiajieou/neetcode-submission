# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = none 
        next = current.next
        arr = []
        while current is not None:
            current.next = prev
            prev = current 
            current = next
            arr.append(prev)
        return arr