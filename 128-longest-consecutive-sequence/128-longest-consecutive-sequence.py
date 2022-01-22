class Solution:
    
    def crange(self,s,n,dirn):
        count = 1
        s.remove(n)
        while (n+(1*dirn)) in s:
            count+=1
            n += 1*dirn
            s.remove(n)
        return count
    
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        longest_sequence_count = 0
        
        
        for n in nums:
            if n in unique_nums:
                count = 1
                unique_nums.remove(n)

                if n-1 in unique_nums:
                    count+= self.crange(unique_nums,n-1,-1)

                if n+1 in unique_nums:
                    count += self.crange(unique_nums,n+1,1)

                if count > longest_sequence_count:
                    longest_sequence_count = count

                if longest_sequence_count > len(unique_nums):
                    return longest_sequence_count
            
        return longest_sequence_count
            