# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive Soln

class Solution:
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        curr = root
        
        while curr != None:
            if curr.left == None:
                res.append(curr.val)
                curr = curr.right
            
            else:
                pre = curr.left
                while pre.right != None and pre.right != curr:
                    pre = pre.right
                
                if pre.right == None:
                    pre.right = curr
                    res.append(curr.val)
                    curr = curr.left
                
                else:
                    pre.right = None
                    curr = curr.right
                    
        return res