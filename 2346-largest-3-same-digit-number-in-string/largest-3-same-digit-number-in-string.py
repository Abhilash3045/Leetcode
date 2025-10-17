class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        res=[]
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                res+=[num[i:i+3]]
        if res:
            x=str(max(list(map(int, res))))
            return "000" if x=="0" else x
        else:
            return ""