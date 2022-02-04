class Solution:
    '''returns the count of numbers less than or equal to mid'''
    def ncalc(self,nums,med):
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = (start + end)//2
            
            if nums[mid] <= med:
                start = mid+1
            
            else:
                end = mid-1
        
        return start 
        
    '''Returns the number which has n integers less than or equal to it'''
    def median_calc(self,nums1,nums2,n):
        
        Min = min(nums1[0],nums2[0])
        Max = max(nums1[-1],nums2[-1])
        
        while Min<=Max:
            mid = (Min+Max)//2
            
            n1 = self.ncalc(nums1,mid)+self.ncalc(nums2,mid)
            
            if n1<=n:
                Min = mid+1
            
            else:
                Max = mid-1
            
        return Min
        
    '''Returns the median of 1D sorted array'''
    def median_calc1(self,nums):
        
        n = len(nums)
        if n%2:
            return nums[n//2]
        
        else:
            return (nums[n//2] + nums[(n//2)-1])/2
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums2) == 0:
            return self.median_calc1(nums1)
        
        elif len(nums1) == 0:
            return self.median_calc1(nums2)
        
        
        n = len(nums1)+len(nums2)
        
        if n%2==0:
            median1 = self.median_calc(nums1,nums2,(n//2))
            median2 = self.median_calc(nums1,nums2,(n//2)-1)
            
            return (median1+median2)/2
        
        else:
            median = self.median_calc(nums1,nums2,n//2)
            return median