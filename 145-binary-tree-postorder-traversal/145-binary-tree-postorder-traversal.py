# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []
        
        ans = []
        stack = []
        stack.append(root)
        
        while len(stack)>0:
            curr = stack.pop()
            if curr.left == None and curr.right == None:
                ans.append(curr.val)
                continue
            
            New_Node = TreeNode(curr.val)
            stack.append(New_Node)
            
            if curr.right != None:
                stack.append(curr.right)
            
            if curr.left != None:
                stack.append(curr.left)
        
        return ans