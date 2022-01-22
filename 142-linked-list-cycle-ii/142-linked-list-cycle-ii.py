# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = head
        hare = head
        
        while True:
            if not hare or not hare.next:
                return None
            
            hare = hare.next.next
            tortoise = tortoise.next
            
            if hare == tortoise:
                break
            
        tortoise = head
        
        while tortoise != hare:
            
            hare = hare.next
            tortoise = tortoise.next
        
        return tortoise