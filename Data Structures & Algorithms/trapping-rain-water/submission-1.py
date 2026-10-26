class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        left_boundary = height[left]
        right_boundary = height[right]

        water = 0

        while left < right:
            
            if left_boundary < right_boundary or left_boundary == right_boundary:
                left += 1
                left_boundary = max(height[left], left_boundary)
                water += left_boundary - height[left]
            
            else:
                right -= 1
                right_boundary = max(height[right], right_boundary)
                water += right_boundary - height[right]
        
        return water