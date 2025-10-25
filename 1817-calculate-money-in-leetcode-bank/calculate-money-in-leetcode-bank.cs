public class Solution {
    public int TotalMoney(int n) {
        int t=0, m=0, i=0, j=0;
        List<int> num = new List<int>{0,1,2,3,4,5,6};
        while (i<n)
        {
            if(i%7==0)
            {
                j=0;
                m++;
            }
            t+=(num[j]+m);
            i++;
            j++;
        }
        return t;
    }
}