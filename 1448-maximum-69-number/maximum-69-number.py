class Solution:
    def maximum69Number (self, num: int) -> int:
        n=str(num)
        l=[];m=True
        for i in range(len(n)):
            if m and n[i]=='6':
                l.append('9')
                m=False
            else:
                l.append(n[i])
        return int("".join(l))