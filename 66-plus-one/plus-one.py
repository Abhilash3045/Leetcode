class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digits=list(map(str, digits))
        # digits="".join(digits)
        # digits=int(digits)+1
        digits=int("".join(list(map(str, digits))))+1
        c=[]
        for i in str(digits):
            c+=[i]
        return list(map(int, c))