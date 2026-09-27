class Solution:
    def reformatNumber(self, number: str) -> str:
        n="";r=""
        for i in number:
            if i.isdigit():
                n+=i
        i=0
        while len(n)-i>4:
            r+=n[i:i+3]+"-"
            i+=3
        
        if len(n)-i==4:
            r+=n[i:i+2]+"-"+n[i+2:i+4]
        else:
            r+=n[i:]
        return r