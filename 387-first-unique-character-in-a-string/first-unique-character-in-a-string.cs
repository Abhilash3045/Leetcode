public class Solution {
    public int FirstUniqChar(string s) {
        Dictionary<char, int> h = new Dictionary<char, int>();
        foreach(char i in s)
        {
            if(h.ContainsKey(i))
            {
                h[i]+=1;
            }
            else
            {
                h[i]=1;
            }
        }
        foreach(KeyValuePair<char, int> kvp in h)
        {
            if(kvp.Value==1)
            {
                return s.IndexOf(kvp.Key);
            }
        }
        return -1;
    }
}