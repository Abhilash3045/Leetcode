class Solution:
    def scoreBalance(self, s: str) -> bool:
        total=sum(ord(c)-ord('a')+1 for c in s)
        p=0
        for i in s:
            p+=ord(i)-ord('a')+1
            if 2*p==total:  return True
        return False