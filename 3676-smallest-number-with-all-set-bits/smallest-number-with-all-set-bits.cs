public class Solution {
    public int SmallestNumber(int n) {
        string binary = Convert.ToString(n, 2);
        string ans = binary.Replace("0", "1");
        return Convert.ToInt32(ans, 2);
    }
}