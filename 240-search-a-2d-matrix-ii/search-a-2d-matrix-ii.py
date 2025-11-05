class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr,nc=len(matrix),len(matrix[0])
        row,col=0,nc-1
        while row<nr and col>=0:
            if matrix[row][col]==target: return True
            elif matrix[row][col]>target: col-=1
            else: row+=1
        return False