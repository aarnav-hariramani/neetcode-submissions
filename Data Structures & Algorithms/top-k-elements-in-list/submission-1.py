class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for val in nums:
            if val not in seen:
                seen[val] = 1
            else:
                seen[val] += 1
        
        return sorted(seen, key=seen.get)[-k:]