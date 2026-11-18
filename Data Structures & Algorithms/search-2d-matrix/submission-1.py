class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        rows = len(matrix)
        columns = len(matrix[0])
        right = rows * columns - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid // columns][mid % columns] > target:
                right = mid - 1
            
            elif matrix[mid //columns][mid % columns] < target:
                left = mid + 1
            
            else:
                return True

        return False


        