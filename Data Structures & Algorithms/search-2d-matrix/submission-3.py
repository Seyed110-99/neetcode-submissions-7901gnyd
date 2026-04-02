class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0

        r = len(matrix) * len(matrix[-1]) - 1

        
        cols = len(matrix[-1])

        while l <= r:

            mid = (l + r)//2

            i = mid // cols
            j = mid % cols

            num = matrix[i][j]

            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return False
        