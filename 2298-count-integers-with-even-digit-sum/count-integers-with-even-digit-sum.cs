public class Solution {
    public int CountEven(int num) {
        int n = num.ToString().Sum(d=>d-'0');
        return (n%2==0) ? num/2 : (num-1)/2;
    }
}