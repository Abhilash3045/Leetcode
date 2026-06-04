public class Solution {
    public int TotalWaviness(int num1, int num2) {
        int Waves(int num){
            string s = num.ToString();
            if(s.Length<3)
                return 0;
            int w=0;
            for(int i=1; i<s.Length-1; i++){
                if((s[i]>s[i-1] && s[i]>s[i+1]) || (s[i]<s[i-1]) && (s[i]<s[i+1]))
                    w+=1;
            }
            return w;
        }
        int t=0;
        for(int x=num1; x<=num2; x++){
            t+=Waves(x);
        }
        return t;
    }
}