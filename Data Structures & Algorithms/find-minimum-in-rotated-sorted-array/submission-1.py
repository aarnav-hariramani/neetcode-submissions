class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_element = nums[0]
        for val in nums:
            min_element = min(val, min_element)
        
        return min_element
        