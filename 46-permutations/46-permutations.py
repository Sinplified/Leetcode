class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.recurPermute(0,nums,ans)
        return ans
    
    def recurPermute(self,index,nums,ans):
        if index == len(nums):
            ans.append(nums[:])
            return
        
        for i in range(index,len(nums)):
            nums[index],nums[i] = nums[i],nums[index]
            self.recurPermute(index+1,nums,ans)
            nums[index],nums[i] = nums[i],nums[index]