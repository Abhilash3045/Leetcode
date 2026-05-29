class Solution:
    def getLucky(self, s: str, k: int) -> int:
        m=""
        for sk in s:
            m+=str((ord(sk.lower()))-ord('a')+1)
        for i in range(k):
            n=0
            for j in m:
                n+=int(j)
            m=str(n)
        return n