class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr,ans = [],[]
        self.Permute(nums,curr,ans)
        
        return ans
    
    def Permute(self,nums,curr,ans):
        if len(nums)==1:
            ans.append(curr+nums)
            return
        
        for i in range(len(nums)):
            curr.append(nums[i])
            self.Permute(nums[:i]+nums[i+1:],curr,ans)
            curr.pop()