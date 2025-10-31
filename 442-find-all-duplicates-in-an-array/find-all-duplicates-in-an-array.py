class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        h,l={},[]
        for i in nums:
            h[i]=h.get(i,0)+1
            if h[i]>1:
                l.append(i)
        return l