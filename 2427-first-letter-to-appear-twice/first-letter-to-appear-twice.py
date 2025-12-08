class Solution:
    def repeatedCharacter(self, s: str) -> str:
        r=[]
        for i in s:
            if i in r: return i
            r.append(i)