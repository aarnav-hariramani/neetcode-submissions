class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, value in enumerate(heights):

            left = i
            while stack and value < stack[-1][1]:
                left = stack[-1][0]
                area = stack[-1][1] * (i - left)
                stack.pop()
                max_area = max(max_area, area)

            stack.append((left, value))
        
        for values in stack:
            area = values[1] * (len(heights) - values[0])
            max_area = max(max_area, area)
        
        return max_area
