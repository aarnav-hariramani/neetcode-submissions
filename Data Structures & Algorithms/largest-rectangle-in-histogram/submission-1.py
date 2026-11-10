class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, value in enumerate(heights):

            left = i
            while stack and value < stack[-1][1]:
                index = stack[-1][0]
                left = index
                area = stack.pop()[1] * (i - left)
                max_area = max(area, max_area)

            stack.append((left, value))
        
        for i in range(len(stack)):
            area = stack[i][1] * (len(heights) - stack[i][0])
            max_area = max(max_area, area)

        return max_area