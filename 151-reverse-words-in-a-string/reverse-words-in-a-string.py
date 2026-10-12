class Solution:
    def reverseWords(self, s: str) -> str:
        r=[]
        for i in list(s.split()):
            r=[i]+r
        return " ".join(r)