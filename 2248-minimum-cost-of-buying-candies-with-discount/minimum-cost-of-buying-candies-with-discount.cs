public class Solution {
    public int MinimumCost(int[] cost) {
        Array.Sort(cost);
        Array.Reverse(cost);
        int t=0;
        for(int i=0; i<cost.Length; i++){
            if(i%3!=2){
                t+=cost[i];
            }
        }
        return t;
    }
}