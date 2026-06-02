public class Solution {
    public int EarliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int minL=3000, minW=3000, res=3000, m=landStartTime.Length, n=waterStartTime.Length;
        for(int i=0; i<m; i++){
            minL=Math.Min(minL, landStartTime[i]+landDuration[i]);
        }
        for(int i=0; i<n; i++){
            minW=Math.Min(minW, waterStartTime[i]+waterDuration[i]);
            res=Math.Min(res, Math.Max(minL, waterStartTime[i])+waterDuration[i]);
        }
        for(int i=0; i<m; i++){
            res=Math.Min(res, Math.Max(minW, landStartTime[i])+landDuration[i]);
        }
        return res;
    }
}