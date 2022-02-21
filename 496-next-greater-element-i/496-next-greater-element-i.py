from queue import LifoQueue

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_dict = dict()
        stack = LifoQueue()
        
        for num in nums2:
            if stack.empty():
                stack.put(num)
                continue
            
            while not stack.empty():
                top = stack.queue[-1]
                
                if top<num:
                    next_dict[stack.get()] = num
                
                else:
                    break
            
            stack.put(num)
        
        ans = [-1]*len(nums1)
        
        for i in range(len(nums1)):
            ans[i] = next_dict.get(nums1[i],-1)
        return ans