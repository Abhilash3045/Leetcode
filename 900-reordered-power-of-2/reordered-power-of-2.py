class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def countd(x):
            return ''.join(sorted(str(x)))
        t=countd(n)
        for i in range(31):
            if countd(1<<i)==t:
                return True
        return False