# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        k = head
        
        while curr.next:
            if n<=0:
                k = k.next
            curr = curr.next
            n-=1
        
        if n>0:
            return head.next
        
        k.next = k.next.next
        return head