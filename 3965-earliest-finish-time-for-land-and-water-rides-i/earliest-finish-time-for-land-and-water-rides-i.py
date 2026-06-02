class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        minL=minW=res=3000
        n=len(landStartTime);m=len(waterStartTime)
        for i in range(n):
            minL=min(minL,landStartTime[i]+landDuration[i])
        for i in range(m):
            minW=min(minW,waterStartTime[i]+waterDuration[i])
            res=min(res,max(minL,waterStartTime[i])+waterDuration[i])
        for i in range(n):
            res=min(res,max(minW,landStartTime[i])+landDuration[i])
        return res