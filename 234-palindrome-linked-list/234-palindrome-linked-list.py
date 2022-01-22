# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def get_len(self,head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length
    
    def Reverse(self,head,k):
        previous = None
        curr = head
        Next = head.next
        
        while k>1:
            curr.next = previous
            previous =curr
            curr = Next
            k-=1
            Next = Next.next
        
        curr.next = previous
        return curr,Next
    
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        Len = self.get_len(head)
        mid = Len//2
        
        if Len <=1:
            return True
        
        Head1,Head2 = self.Reverse(head,mid)
        
        if Len%2:
            Head2 = Head2.next
        
        while Head1:
            if Head1.val != Head2.val:
                return False
            
            Head1 = Head1.next
            Head2 = Head2.next
        
        return True