class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack,cnum,cstr=[],0,''
        for c in s:
            if c=='[':
                stack.append(cstr)
                stack.append(cnum)
                cstr,cnum='',0
            elif c==']':
                num=stack.pop()
                pstr=stack.pop()
                cstr=pstr+num*cstr
            elif c.isdigit():
                cnum=cnum*10+int(c)
            else:
                cstr+=c
        return cstr