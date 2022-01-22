class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.cSum(candidates,target,0,[])
        
    def cSum(self,candidates,target,ind,ans):
        
        if ind == len(candidates) or candidates[ind]>target:
            return []
        
        if candidates[ind] == target:
            return [ans+[candidates[ind]]]
        
        including = self.cSum(candidates,target-candidates[ind],ind,ans+[candidates[ind]])
        excluding = self.cSum(candidates,target,ind+1,ans)
        
        return including + excluding