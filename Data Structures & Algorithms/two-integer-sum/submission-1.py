class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, value in enumerate(nums):
            complement = target - value
            if complement in lookup:
                return [lookup[complement], i]
            lookup[value] = i