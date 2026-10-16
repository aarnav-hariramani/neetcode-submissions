class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sort = sorted(nums)
        output = []

        for i in range(len(nums_sort)):
            j = i + 1
            k = len(nums_sort) - 1

            if i > 0 and nums_sort[i] == nums_sort[i - 1]:
                continue

            while j < k:
                if nums_sort[j] + nums_sort[k] > -(nums_sort[i]):
                    k -= 1
                
                elif nums_sort[j] + nums_sort[k] < -(nums_sort[i]):
                    j += 1

                else:
                    output.append([nums_sort[j], nums_sort[k], nums_sort[i]])
                    j += 1
                    k -= 1
                    while j < k and nums_sort[j] == nums_sort[j-1]:
                            j += 1
        
        return output        