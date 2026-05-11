public class Solution {
    public int AddDigits(int num) {
        while(num>9){
            int n = num.ToString().Sum(d=>d-'0');
            num=n;
        }
        return num;
    }
}