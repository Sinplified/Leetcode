# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def help_traverse(self,root,L):                
        
        if root.left != None:
            self.help_traverse(root.left,L)
            
        if root.right!=None:
            self.help_traverse(root.right,L)
            
        L.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []
        
        L = []
        
        self.help_traverse(root,L)
        
        return L