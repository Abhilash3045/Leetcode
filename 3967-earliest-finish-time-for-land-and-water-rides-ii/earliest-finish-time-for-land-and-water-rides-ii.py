class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        minL=minW=res=float('inf')
        m=len(landStartTime);n=len(waterStartTime)
        for i in range(m):
            minL=min(minL, landStartTime[i]+landDuration[i])
        for i in range(n):
            minW=min(minW, waterStartTime[i]+waterDuration[i])
            res=min(res, max(minL, waterStartTime[i])+waterDuration[i])
        for i in range(m):
            res=min(res, max(minW, landStartTime[i])+landDuration[i])
        return res