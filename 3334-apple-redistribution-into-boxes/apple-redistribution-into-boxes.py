class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        t=sum(apple)
        capacity.sort(reverse=True)
        c=0
        for i in capacity:
            t-=i
            c+=1
            if t<=0:
                return c
        return c