class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        cap=0
        while j>i:
            m=j-i
            cap=max(m*min(height[i],height[j]), cap)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return cap