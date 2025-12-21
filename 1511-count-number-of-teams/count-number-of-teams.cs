public class Solution {
    public int NumTeams(int[] rating) {
        int n = rating.Length, res = 0;
        for(int j = 0; j<n; j++){
            int ls=0,ll=0,rs=0,rl=0;
            for(int i=0; i<j; i++){
                if(rating[i]>rating[j]) ll++;
                else    ls++;
            }
            for(int k=j+1; k<n; k++){
                if(rating[k]>rating[j]) rl++;
                else    rs++;
            }
            res+=(ls*rl)+(ll*rs);
        }
        return res;
    }
}