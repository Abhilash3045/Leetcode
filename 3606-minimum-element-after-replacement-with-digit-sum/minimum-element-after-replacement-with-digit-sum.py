class Solution:
    def minElement(self, nums: List[int]) -> int:
        r=[sum(int(d) for d in str(num)) for num in nums]
        r.sort()
        return r[0]