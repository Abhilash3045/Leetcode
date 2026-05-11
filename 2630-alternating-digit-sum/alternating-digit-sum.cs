public class Solution {
    public int AlternateDigitSum(int n) {
        int c=0;
        string s=n.ToString();
        for(int i=0; i<s.Length; i++){
            c+= (i%2==0) ? s[i]-'0' : -(s[i]-'0');
        }
        return c;
    }
}