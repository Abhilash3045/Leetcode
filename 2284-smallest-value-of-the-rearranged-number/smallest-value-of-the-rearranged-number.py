class Solution:
    def smallestNumber(self, num: int) -> int:
        s=-1 if num<0 else 1
        num=list(str(num))
        if s!=1:
            num=num[1:]
            num.sort(reverse=True)
            return s*int("".join(num))
        else:
            num.sort()
            if num[0]=='0':
                for i in range(1,len(num)):
                    if num[i]!='0':
                        num[0],num[i]=num[i],num[0]
                        break
            return int("".join(num))
