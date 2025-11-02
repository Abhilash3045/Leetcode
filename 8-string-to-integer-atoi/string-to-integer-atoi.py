class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        a = '1234567890'
        p = ""
        sign,i = 1,0
        low = -2**31
        high = (2**31)-1
        if not s:
            return 0
        if s[0]=='-':
            sign = -1
            i+=1
        elif s[0]=='+':
            i+=1
        
        while i<len(s) and s[i] in a:
            p+=s[i]
            i+=1
        if not p:
            return 0
        
        ap = sign * int(p)
        if ap < low:
            return low
        elif ap > high:
            return high
        return ap