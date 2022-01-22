class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <=2:
            return []
        nums.sort()
        ans = []
        for i in range(n-2):
            if i==0 or nums[i-1] != nums[i]:
                j = i+1
                k = n-1
                
                while j<k:
                    if nums[j]+nums[k]+nums[i] == 0:
                        ans.append([nums[i],nums[j],nums[k]])
                    
                        while j<k and nums[j]==nums[j+1]:
                            j+=1

                        while k>j and nums[k] == nums[k-1]:
                            k-=1

                        j+=1
                        k-=1
                    
                    elif nums[j]+nums[k]+nums[i]<0:
                        j+=1
                    
                    else:
                        k-=1
        
        return ans
                    