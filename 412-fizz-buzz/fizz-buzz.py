class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]
        for i in range(1,n+1):
            t=""
            if i%3==0:
                t+="Fizz"
            if i%5==0:
                t+="Buzz"
            if t!="":
                res.append(t)
            else:
                res.append(str(i))
        return res