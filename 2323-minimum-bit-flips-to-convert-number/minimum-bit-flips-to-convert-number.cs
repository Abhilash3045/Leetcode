public class Solution {
    public int MinBitFlips(int start, int goal) {
        int xor = start ^ goal;
        return Convert.ToString(xor, 2).Count(c=>c=='1');
    }
}