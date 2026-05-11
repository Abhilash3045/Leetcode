class Solution:
    def alternateDigitSum(self, n: int) -> int:
        c=0
        n=str(n)
        for i in range(len(n)):
            if i%2==0:
                c+=int(n[i])
            else:
                c-=int(n[i])
        return c