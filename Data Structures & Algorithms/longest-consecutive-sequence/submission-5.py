class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_final = set(nums)
        counter = 0
        final = 0

        for val in nums_final:
            if val - 1 in nums_final:
                continue
            
            counter = 1
            while val + 1 in nums_final:
                counter += 1
                val += 1
                
            final = max(final, counter)
        
        return final
            
            
            

        