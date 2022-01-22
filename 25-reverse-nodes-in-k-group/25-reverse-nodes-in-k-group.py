# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def get_len(self,head):
        Len = 0
        while head:
            head = head.next
            Len +=1
        
        return Len
    
    def Reverse(self,head,k):
        previous = None
        curr = head
        Next = curr.next
        
        while k>1:
            
            curr.next = previous
            previous = curr
            curr = Next
            Next = Next.next
            k-=1
        
        curr.next = previous
        
        return curr,Next
    
    def rev_k_rec(self,head,k,Len):
        if k>Len:
            return head
        
        Head,R_head = self.Reverse(head,k)
        
        head.next = self.rev_k_rec(R_head,k,Len-k)
        
        return Head
            
            
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        Len = self.get_len(head)
        return self.rev_k_rec(head,k,Len)