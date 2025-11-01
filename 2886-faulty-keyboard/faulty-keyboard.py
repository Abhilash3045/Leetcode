class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        p=""
        for i in s:
            if i=="i":
                p=p[::-1]
            else:
                p+=i
        return p