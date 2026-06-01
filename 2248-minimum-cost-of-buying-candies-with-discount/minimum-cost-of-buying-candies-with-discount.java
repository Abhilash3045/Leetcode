class Solution {
    public int minimumCost(int[] cost) {
        Arrays.sort(cost);
        int t=0,m=0;
        for(int i=cost.length-1;i>=0;i--){
            if(m%3!=2){
                t+=cost[i];
            }
            m++;
        }
        return t;
    }
}