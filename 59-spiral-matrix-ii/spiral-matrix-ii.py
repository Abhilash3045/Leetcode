class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat=[[0]*n for _ in range(n)]
        top,left=0,0
        k=1
        bottom,right=len(mat)-1,len(mat[0])-1
        while top<=bottom and left<=right:
            for i in range(left, right+1):
                mat[top][i]=k
                k+=1
            top+=1
            for i in range(top, bottom+1):
                mat[i][right]=k
                k+=1
            right-=1
            if top<=bottom:
                for i in range(right, left-1, -1):
                    mat[bottom][i]=k
                    k+=1
                bottom-=1
            if left<=right:
                for i in range(bottom, top-1,-1):
                    mat[i][left]=k
                    k+=1
                left+=1
        return mat