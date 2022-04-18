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
        
        while curr!= None:
            if curr.left == None:
                res.append(curr.val)
                curr = curr.right
            
            else:
                pre = curr.left
                while pre.right!= None and pre.right != curr:
                    pre = pre.right
                
                if pre.right == None:
                    pre.right = curr
                    curr = curr.left
                
                else:
                    pre.right = None
                    res.append(curr.val)
                    curr = curr.right
        
        return res