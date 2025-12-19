class Solution:
    def modifyString(self, s: str) -> str:
        alp="abcdefghijklmnopqrstuvwxyz"
        res=[]
        for i in range(len(s)):
            ind=0
            if s[i]=='?':
                if i==0:
                    if len(s)==1:
                        return "a"
                    while s[i+1]==alp[ind]:
                        ind+=1
                    res.append(alp[ind])
                elif i==len(s)-1:
                    while s[i-1]==alp[ind] or res[-1]==alp[ind]:
                        ind+=1
                    res.append(alp[ind])
                else:
                    while s[i-1]==alp[ind] or s[i+1]==alp[ind] or res[-1]==alp[ind]:
                        ind+=1
                    res.append(alp[ind])
            else:
                res.append(s[i])
        return "".join(res)