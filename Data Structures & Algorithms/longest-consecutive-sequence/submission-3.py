class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # nums_set={2,20,10,3,4,5}

        final = 0
        for val in nums_set:
            if val - 1 in nums_set:
                continue
            
            counter = 1
            current = val
            while current + 1 in nums_set:
                counter += 1
                current += 1

            final = max(counter, final)
        return final



        