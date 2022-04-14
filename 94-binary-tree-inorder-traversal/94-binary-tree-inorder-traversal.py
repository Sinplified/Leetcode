# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def help_traverse(self,root,L):
        
        if root.left == None and root.right == None:
            L.append(root.val)
            return
        
        if root.left != None:                  #Left Traversal
            self.help_traverse(root.left,L)
        
        L.append(root.val)                     #Inorder
        
        if root.right != None:                 #Right Traversal
            self.help_traverse(root.right,L)
            
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            
            return []
        
        L = []
        
        self.help_traverse(root,L)
        
        return L