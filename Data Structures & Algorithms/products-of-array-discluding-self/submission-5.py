class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        running = 1

        for i in range(len(result)):
            result[i] = running
            running *= nums[i]
        
        running = 1
        for val in range(len(result) - 1, - 1, - 1):
            result[val] *= running
            running *= nums[val]

        return result
        