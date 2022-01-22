class Solution:
    
    def cSum2(self,candidates,ind,target,curr):
        if target == 0:
            return [curr[:]]
        
        if ind == len(candidates):
            return []
        
        ans = []
        
        for i in range(ind,len(candidates)):
            if i == ind or candidates[i]!=candidates[i-1]:
                
                if candidates[i]<= target:
                    curr.append(candidates[i])
                    ans += self.cSum2(candidates,i+1,target-candidates[i],curr)
                    curr.pop()
                else:
                    break
        return ans
    
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        return self.cSum2(candidates,0,target,[])