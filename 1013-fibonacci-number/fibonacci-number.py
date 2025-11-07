class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b=0,1
        c=[]
        for _ in range(n+1):
            c+=[a]
            a,b=b,a+b
        return c[-1]
        # if n<=1:
        #     return n
        # elif n==2:
        #     return 1
        # return self.fib(n-2)+self.fib(n-1)