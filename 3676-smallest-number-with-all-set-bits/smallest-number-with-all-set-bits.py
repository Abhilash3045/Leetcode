class Solution:
    def smallestNumber(self, n: int) -> int:
        r = str(bin(n)[2:])
        return int("1"*len(r), 2)