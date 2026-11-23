class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, value in enumerate(heights):

            left = i
            while stack and value < stack[-1][1]:
                left = stack[-1][0]
                area = stack.pop()[1] * (i - left)
                max_area = max(area, max_area)

            stack.append((left, value))

        for value in stack:
            area = (len(heights) - value[0]) * value[1]
            max_area = max(area, max_area)
        
        return max_area

        