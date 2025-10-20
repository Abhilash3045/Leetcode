class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n=[nums[0]]
        for num in nums[1:]:
            if num != n[-1]:
                n.append(num)
        hills=0
        for i in range(1,len(n)-1):
            if n[i]>n[i-1] and n[i]>n[i+1]:
                hills+=1
            elif n[i]<n[i-1] and n[i]<n[i+1]:
                hills+=1
        return hills