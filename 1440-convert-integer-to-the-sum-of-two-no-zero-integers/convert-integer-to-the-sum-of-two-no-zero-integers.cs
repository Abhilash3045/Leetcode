public class Solution {
    public int[] GetNoZeroIntegers(int n) {
        bool check(int x)
        {
            return !x.ToString().Contains('0');
        }
        for(int i = 0; i <= n; i++)
        {
            int j = n - i;
            if(check(i) && check(j))
            {
                return new int[] {i, j};
            }
        }
        return new int[] { };
    }
}