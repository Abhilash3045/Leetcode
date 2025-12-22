public class Solution {
    public int MinimumMoves(string s) {
        int ans=0,i=0;
        while(i<s.Length){
            if(s[i]=='X'){
                ans+=1;
                i+=3;
            }
            else    i+=1;
        }
        return ans;
    }
}