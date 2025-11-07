class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1: return n
        elif n==2: return 1
        a,b,c = 0,1,1
        for i in range(2,n):
            a,b,c=b,c,a+b+c
        return c
        # return self.tribonacci(n-3)+self.tribonacci(n-2)+self.tribonacci(n-1)