class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_final = set(nums)

        final = 0

        for val in nums_final:

            if val - 1 in nums_final:
                continue

            count = 1

            while val + 1 in nums_final:
                count += 1
                val += 1

            final = max(final, count)

        return final
                    