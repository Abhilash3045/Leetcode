class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row=len(grid)-1;c=0
        while row>=0:
            col=len(grid[0])-1
            while grid[row][col]<0 and col>=0:
                c+=1
                col-=1
            row-=1
        return c