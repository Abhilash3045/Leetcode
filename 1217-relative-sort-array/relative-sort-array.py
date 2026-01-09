class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        h={};a=[];t=[]
        for i in arr1:
            h[i]=h.get(i,0)+1
        for i in arr2:
            a+=[i]*h[i]
            h[i]=0
        for i in h:
            if h[i]!=0:
                t+=[i]*h[i]
        t.sort()
        return a+t