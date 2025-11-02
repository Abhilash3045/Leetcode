class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]=="R":
                    r,c=i,j
        res=0
        for dr,dc in directions:
            i,j=r+dr,c+dc
            while 0<=i<8 and 0<=j<8:
                if board[i][j]=='p': res+=1
                if board[i][j]!='.': break
                i,j=i+dr,j+dc
        return res