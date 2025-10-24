class Solution:
    def firstUniqChar(self, s: str) -> int:
        h={}
        for i in s:
            h[i]=h.get(i, 0)+1
        for key, value in h.items():
            if value==1: return s.index(key)
        return -1