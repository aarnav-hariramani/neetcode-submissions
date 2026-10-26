class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        product = 1
        count = 0

        for val in nums:
            if val == 0:
                count += 1
            else:
                product *= val

        for i in range(len(nums)):
            if count > 1:
                return output
            elif count == 1:
                if nums[i] == 0:
                    output[i] = product
                else:
                    output[i] = 0
            else:
                output[i] = int(product / nums[i])
        
        return output
        