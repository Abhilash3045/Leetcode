class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def ap(x:int)->bool:
            p=x
            while p:
                k=p%10
                if k==0:
                    return False
                else:
                    if x%k!=0: return False
                p//=10
            return True
        res=[]
        for p in range(left,right+1):
            if ap(p): res.append(p)
        return res