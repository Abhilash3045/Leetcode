class Solution:
    def totalMoney(self, n: int) -> int:
        t,m=0,0
        ml=[0,1,2,3,4,5,6]
        i,j=0,0
        while i<n:
            if i%7==0:
                j=0
                m+=1
            t+=(ml[j]+m)
            j+=1
            i+=1
        return t

        