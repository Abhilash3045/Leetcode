class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(1,n):
            temp=s
            inv=''.join('1' if c=='0' else '0' for c in temp)
            s=s+'1'+(inv[::-1])
        return s[k-1]