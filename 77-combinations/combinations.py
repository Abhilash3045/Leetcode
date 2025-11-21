class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        r=[]
        for i in range(1,n+1):
            r+=[i]
        m=list(combinations(r,k))
        return m