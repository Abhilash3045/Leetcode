class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=0,0
        while row<len(matrix):
            if matrix[row][col]==target:
                return True
            col+=1
            if col==len(matrix[0]):
                col=0
                row+=1
        return False