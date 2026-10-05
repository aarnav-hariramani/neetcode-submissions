class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        running = 1

        for i in range(len(nums)):
            result[i] = running
            running *= nums[i]
            
        running = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= running
            running *= nums[i]

            
        
        return result


        '''
        # This is the division way
        result = [0] * len(nums)
        non_zero_product = 1
        product = 1

        for val in nums:
            if val != 0:
                non_zero_product *= val
                
        for val in nums:
            product *= val
        
        if nums.count(0) > 1:
            return result
        
        for i in range(len(nums)):
            if nums[i] == 0:
                result[i] = non_zero_product
                return result

            result[i] = int(product / nums[i])

        return result
        '''
            