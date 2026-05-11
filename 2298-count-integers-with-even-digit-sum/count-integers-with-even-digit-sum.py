class Solution:
    def countEven(self, num: int) -> int:
        n=sum(int(d) for d in str(num))
        return num//2 if n%2==0 else (num-1)//2