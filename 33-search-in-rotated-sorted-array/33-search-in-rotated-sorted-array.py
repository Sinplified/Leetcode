class Solution:
    
    def bsearch(self,nums,start,end,target):
        while start<=end:
            mid = (start+end)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid]<target:
                start = mid+1
            
            else:
                end = mid-1
                
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1        
        rotation = -1
        
        while l<=r:
            mid = (l+r)//2
            
            if mid+1 > len(nums)-1:
                break
            
            if nums[mid]> nums[mid+1]:
                rotation = mid+1
                break
            
            else:
                
                if nums[mid]<nums[0]:
                    r = mid-1
                    
                else:
                    l = mid+1
        
        
        if rotation == -1:
            return self.bsearch(nums,0,len(nums)-1,target)
        
        elif target<nums[0]:
            return self.bsearch(nums,rotation,len(nums)-1,target)
        
        else:
            return self.bsearch(nums,0,rotation-1,target)
        