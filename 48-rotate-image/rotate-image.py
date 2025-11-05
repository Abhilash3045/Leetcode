class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp=[row[:] for row in matrix]
        right=len(matrix[0])-1
        row,col=0,0
        while right>=0:
            matrix[col][right]=temp[row][col]
            col+=1
            if col==len(matrix):
                col=0
                row+=1
                right-=1