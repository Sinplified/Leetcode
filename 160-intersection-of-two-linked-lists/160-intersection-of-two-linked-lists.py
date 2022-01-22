# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def get_len(self,head):
        length = 0
        while head:
            length +=1
            head = head.next
        
        return length
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = self.get_len(headA)
        lenB = self.get_len(headB)
        
        if lenA<lenB:
            lenB,lenA = lenA,lenB
            headA,headB = headB,headA
            
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        
        while headA:
            if headA == headB:
                return headA
            
            headA = headA.next
            headB = headB.next
        
        return None