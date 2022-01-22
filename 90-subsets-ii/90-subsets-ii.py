class Solution:
    def rec(self,st,cur,arr,subsets):
        subsets.append(cur[:])
        for i in range(st,len(arr)):
            if i==st or arr[i] != arr[i-1]:
                cur.append(arr[i])
                self.rec(i+1,cur,arr,subsets)
                cur.pop()
        
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        cur = []
        self.rec(0,cur,nums,subsets)
        
        return subsets