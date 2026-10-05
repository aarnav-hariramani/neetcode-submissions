class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        index = {}

        for num in nums:
            if num not in index:
                index[num] = 1
            else:
                index[num] += 1

        top_k = sorted(index, key=index.get)[-k:]

        return top_k




        
        