class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}
        for i, value in enumerate(nums):
            complement = target - value
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[value] = i