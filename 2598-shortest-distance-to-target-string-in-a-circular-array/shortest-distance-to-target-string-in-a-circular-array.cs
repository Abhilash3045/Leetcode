public class Solution {
    public int ClosestTarget(string[] words, string target, int startIndex) {
        if(!words.Contains(target))
            return -1;
        int n=words.Length;
        int ans=int.MaxValue;
        for(int i=0;i<n;i++){
            if(words[i]==target){
                int d = Math.Abs(i-startIndex);
                ans = Math.Min(ans,Math.Min(d,n-d));
            }
        }
        return ans;
    }
}