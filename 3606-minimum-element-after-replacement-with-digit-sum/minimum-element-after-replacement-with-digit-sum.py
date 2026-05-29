class Solution:
    def minElement(self, nums: List[int]) -> int:
        r=[]
        for num in nums:
            ds=0
            for d in str(num):
                ds+=int(d)
            r.append(ds)
        r.sort()
        return r[0]