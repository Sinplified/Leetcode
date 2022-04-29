# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    
    def helper(self,arr,ind,val):
        if len(arr)>ind:
            arr[ind].append(val)
        
        else:
            arr.append([val])
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        pos = []
        neg = []
        
        q = Queue(maxsize = 1000)
        
        q.put((root,0,0))
        
        while not q.empty():
            
            curr = q.get()
            node = curr[0]
            ver_ind = curr[1]
            horiz_ind = curr[2]
            
            if horiz_ind >=0:
                self.helper(pos,horiz_ind,(node.val,ver_ind))
            
            else:
                ind = (horiz_ind+1)*(-1)
                self.helper(neg,ind,(node.val,ver_ind))
            
            if node.left:
                q.put((node.left,ver_ind+1,horiz_ind-1))
            
            if node.right:
                q.put((node.right,ver_ind+1,horiz_ind+1))
        
        neg.reverse()
        ans = neg + pos
        for arr in ans:
            arr.sort(key = lambda x: (x[1],x[0]))
        
        real_ans = [[x[0] for x in arr] for arr in ans]
        
        return real_ans