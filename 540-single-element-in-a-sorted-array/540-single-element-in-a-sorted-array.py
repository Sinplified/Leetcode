class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            if l == r:
                return nums[l]
            
            mid = (l+r)//2
            lmid = mid-1
            rmid = mid+1
            
            if nums[lmid] == nums[mid]:
                if lmid%2:
                    r = lmid-1
                else:
                    l = mid+1
            
            elif nums[rmid] == nums[mid]:
                if rmid%2:
                    l = rmid+1
                else:
                    r = mid-1
                
            else:
                l = mid
                r = mid