public class Solution {
    public int AreaOfMaxDiagonal(int[][] dimensions) {
        double temp = 0;
        int ans = 0;
        foreach(var d in dimensions)
        {
            int x=d[0];
            int y=d[1];
            double tmp = Math.Sqrt(x*x+y*y);
            int an = x*y;
            if(tmp>temp)
            {
                temp=tmp;
                ans=an;
            }
            else if(tmp==temp)
            {
                ans=Math.Max(an, ans);
            }
        }
        return ans;
    }
}