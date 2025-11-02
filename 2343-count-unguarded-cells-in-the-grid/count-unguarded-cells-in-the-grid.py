class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[0]*n for _ in range(m)]
        for r,c in guards:
            grid[r][c]=2
        for r,c in walls:
            grid[r][c]=2
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for gr,gc in guards:
            for dr,dc in directions:
                r,c=gr+dr,gc+dc
                while 0<=r<m and 0<=c<n and grid[r][c]!=2:
                    grid[r][c]=1
                    r+=dr
                    c+=dc
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    count+=1
        return count