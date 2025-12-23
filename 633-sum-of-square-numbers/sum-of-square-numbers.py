class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        div=2
        while div*div<=c:
            if c%div==0:
                ec=0
                while c%div==0:
                    ec+=1
                    c//=div
                if div%4==3 and ec%2!=0:    return False
            div+=1
        return c%4!=3