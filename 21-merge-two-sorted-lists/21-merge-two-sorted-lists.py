# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        Head1 = list1
        Head2 = list2
        
        if not Head1 and not Head2:
            return Head1
        
        elif not Head1:
            return Head2
        
        elif not Head2:
            return Head1
        
        if Head1.val<= Head2.val:
            Head = Head1
            curr = Head1
            Head1 = Head1.next
        else:
            Head = Head2
            curr = Head2
            Head2 = Head2.next
        
        
        while Head1 and Head2:
            num1 = Head1.val
            num2 = Head2.val
            
            if num1<=num2:
                curr.next = Head1
                curr = curr.next
                Head1 = Head1.next
            
            else:
                curr.next = Head2
                curr = curr.next
                Head2 = Head2.next
            
        if not Head1:
            curr.next = Head2
        
        if not Head2:
            curr.next = Head1
            
        return Head