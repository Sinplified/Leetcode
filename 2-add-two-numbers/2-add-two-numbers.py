# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def Node_generator(self,Sum,curr):
        digit = Sum%10
        carry = Sum//10
        Node = ListNode(digit)
        curr.next = Node
        return carry
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        curr = head
        while l1 and l2:
            Sum = l1.val + l2.val + carry
            carry = self.Node_generator(Sum,curr)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
    
        while l1:
            Sum = l1.val + carry
            carry = self.Node_generator(Sum,curr)
            l1 = l1.next
            curr = curr.next
        
        while l2:
            Sum = l2.val + carry
            carry = self.Node_generator(Sum,curr)
            l2 = l2.next
            curr = curr.next
        
        if carry == 1:
            Node = ListNode(carry)
            curr.next = Node
        
        return head.next