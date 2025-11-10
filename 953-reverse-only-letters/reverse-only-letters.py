class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev=""
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                rev+=s[i]
        s=list(s)
        i,j=0,0
        while i<len(s):
            if s[i].isalpha():
                s[i]=rev[j]
                j+=1
            i+=1
        return "".join(s)
        