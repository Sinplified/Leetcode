# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive Soln

class Solution:
    
    def help_traverse(self,root,L):        
        if root.left == None and root.right == None:
            L.append(root.val)
            return
        
        L.append(root.val)
        if root.left != None:
            self.help_traverse(root.left,L)
            
        if root.right!=None:
            self.help_traverse(root.right,L)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []
        
        L = []
        
        self.help_traverse(root,L)
        
        return L