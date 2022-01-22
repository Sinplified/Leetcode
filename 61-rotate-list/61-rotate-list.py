# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def getlen(self,head):
        curr = head
        length = 0
        while curr:
            length +=1
            curr = curr.next

        return length
    
#     def Reverse(self,head):
#         previous = None
#         curr = head
#         while curr:
#             Next = curr.next
#             curr.next = previous
#             curr = Next
        
#         return previous,head
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        Len = self.getlen(head)
        k = k%Len
        if k==0:
            return head
        
        Len = Len - k -1
        curr = head
        
        while Len>0:
            curr = curr.next
            Len -=1
        
        Head = curr.next
        curr.next = None
        tail = Head
        while tail.next:
            tail = tail.next
            
        tail.next = head
        
        return Head
        
        
        
        
        
        
        
        
        