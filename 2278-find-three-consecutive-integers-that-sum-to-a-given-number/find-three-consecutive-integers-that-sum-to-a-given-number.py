class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res=[]
        if (num-3)%3==0:
            x=(num-3)//3
            res.append(x)
            res.append(x+1)
            res.append(x+2)
        return res