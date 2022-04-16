# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive Soln

class Solution:
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []
        
        stack = []
        ans= []
        stack.append(root)
        
        while(len(stack)>0):
            curr = stack.pop()
            ans.append(curr.val)
            
            if curr.right != None:
                stack.append(curr.right)
            
            if curr.left != None:
                stack.append(curr.left)
                
        return ans