class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        left_boundary, right_boundary = height[left], height[right]
        water = 0

        while left < right:

            if left_boundary < right_boundary or left_boundary == right_boundary:
                left += 1
                left_boundary = max(left_boundary, height[left])
                water += left_boundary - height[left] 
            
            else:
                right -= 1
                right_boundary = max(right_boundary, height[right])
                water += right_boundary - height[right]

        return water
        
            
            
            