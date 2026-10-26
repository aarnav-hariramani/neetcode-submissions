class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        running = 1

        for i in range(len(nums)):
            output[i] = running
            running *= nums[i]

        running = 1    
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= running
            running *= nums[i]

        return output