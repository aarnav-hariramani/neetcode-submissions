class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_limit = max(piles)
        left = 1

        min_speed = max_limit
        
        while left <= max_limit:
            hours = 0
            mid = (max_limit + left) // 2

            for values in piles:
                hours += -(-values // mid)
            
            if hours > h:
                left = mid + 1
            else:
                min_speed = min(min_speed, mid)
                max_limit = mid - 1

        return min_speed

