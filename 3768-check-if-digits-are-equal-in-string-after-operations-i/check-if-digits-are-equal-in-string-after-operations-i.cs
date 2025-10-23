public class Solution {
    public bool HasSameDigits(string s) {
        while(s.Length>2)
        {
            var st = new StringBuilder();
            for(int i=1; i < s.Length; i++)
            {
                int n = (s[i-1]-'0' + s[i]-'0')%10;
                st.Append(n);
            }
            s=st.ToString();
        }
        return s[0]==s[s.Length-1];
    }
}