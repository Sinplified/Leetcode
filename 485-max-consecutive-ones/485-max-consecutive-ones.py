class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Max_ones = 0
        sum1 = 0
        for i in nums:
            sum1 = sum1*i + i
            
            if sum1>Max_ones:
                Max_ones = sum1
        
        return Max_ones
            