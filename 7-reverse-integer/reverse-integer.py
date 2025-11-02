class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x[0]=='-':
            p = int(x[1:][::-1])
            p=-p
        else:
            p=int(x[::-1])
        if p>(-2)**31 and p<(2**31)-1:
            return p
        return 0