class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        h={}
        for i in stones:
            h[i]=h.get(i,0)+1
        c=0
        for i in jewels:
            if i in h:
                c+=h[i]
        return c