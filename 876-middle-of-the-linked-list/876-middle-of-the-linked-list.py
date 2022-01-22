# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        x= head
        twox = head
        
        while twox != None and twox.next != None:
            twox = twox.next.next
            x = x.next
        
        return x
            