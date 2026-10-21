class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums_sort = sorted(nums)
        output = []

        for i in range(len(nums_sort)):
            
            if i > 0 and nums_sort[i] == nums_sort[i-1]:
                continue

            j = i + 1
            k = len(nums_sort) - 1

            while j < k:
                if nums_sort[j] + nums_sort[k] > -(nums_sort[i]):
                    k -= 1
                elif nums_sort[j] + nums_sort[k] < -(nums_sort[i]):
                    j += 1
                else:
                    output.append([nums_sort[i],nums_sort[j],nums_sort[k]])
                    j += 1
                    k -= 1
                    while nums_sort[j] == nums_sort[j - 1] and j < k:
                        j += 1
        return output