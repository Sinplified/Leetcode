class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        
        i = 0
        k = 1
        for p in range(1,len(nums)):
            if nums[p] != nums[i]:
                k+=1
                i+=1
                nums[p],nums[i] = nums[i],nums[p]
        
        return k