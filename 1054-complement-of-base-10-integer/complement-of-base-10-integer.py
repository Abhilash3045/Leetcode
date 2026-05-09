class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n=bin(n)[2:];k=""
        for i in n:
            if i=="1":  k+="0"
            else:   k+="1"
        return int(k, 2)