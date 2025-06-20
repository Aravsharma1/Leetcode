class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in range(len(matrix)):
            low = 0
            high = len(matrix[x]) - 1
            while(low <= high):
                mid = (low + high) // 2
                if matrix[x][mid] == target:
                    return True
                elif (matrix[x][mid] > target):
                    high -= 1
                else:
                    low += 1
        return False