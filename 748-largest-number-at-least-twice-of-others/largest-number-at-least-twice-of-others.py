class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        num=sorted(nums)
        return nums.index(num[-1]) if num[-1]>=2*num[-2] else -1