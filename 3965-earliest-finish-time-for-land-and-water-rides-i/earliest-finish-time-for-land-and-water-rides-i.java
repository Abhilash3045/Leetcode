class Solution {
    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int minL, minW, res;
        minL=minW=res=100000000;
        int n=waterStartTime.length, m=landStartTime.length;
        for(int i=0; i<m; i++){
            minL=Math.min(minL, landStartTime[i]+landDuration[i]);
        }
        for(int i=0; i<n; i++){
            minW=Math.min(minW, waterStartTime[i]+waterDuration[i]);
            res=Math.min(res,Math.max(minL, waterStartTime[i])+waterDuration[i]);
        }
        for(int i=0; i<m; i++){
            res=Math.min(res,Math.max(minW, landStartTime[i])+landDuration[i]);
        }
        return res;
    }
}