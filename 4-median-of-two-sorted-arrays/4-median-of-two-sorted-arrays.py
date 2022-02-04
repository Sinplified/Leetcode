class Solution:
    
    def median(self,nums1,nums2,m,n):
        
        if m>n:
           return self.median(nums2,nums1,n,m) 
        
        low , high = 0 , m
        medianPos = ((m+n)+1)//2
        
        while low <= high:
            cut1 = (low+high)>>1
            cut2 = medianPos - cut1
            
            l1 = -(10**7) if cut1==0 else nums1[cut1-1]
            l2 = -(10**7) if cut2==0 else nums2[cut2-1]
            r1 =  (10**7) if cut1==m else nums1[cut1]
            r2 =  (10**7) if cut2==n else nums2[cut2]
            
            
            if l1<=r2 and l2<=r1:
                if (m+n)%2:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            
            elif l1>r2:
                high = cut1-1
            
            else:
                low = cut1+1
        
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.median(nums1,nums2,len(nums1),len(nums2))