# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        curr = root
        pre  = None
        
        while curr!= None:
            if curr.left == None:
                res.append(curr.val)
                curr = curr.right
            
            else:
                pre = curr.left
                while pre.right!= None:
                    pre = pre.right
                pre.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
        
        return res