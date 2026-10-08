class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        running = 1

        for i in range(len(nums)):
            result[i] = running
            running *= nums[i]
        
        running = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= running
            running *= nums[i]
    
        return result