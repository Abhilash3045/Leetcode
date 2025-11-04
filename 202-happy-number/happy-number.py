def calculate(p):
    a = 0
    while p!=0:
        digit = p%10
        a += digit**2
        p//=10
    return a
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = calculate(n)
        return True if n==1 else False