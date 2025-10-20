public class Solution {
    public int MaxFreqSum(string s) {
        string vowels = "aeiou";
        string consonants = "bcdfghjklmnpqrstvwxyz";
        Dictionary<char, int> v = new Dictionary<char, int>();
        Dictionary<char, int> c = new Dictionary<char, int>();
        foreach(char i in s)
        {
            if(vowels.Contains(i))
            {
                v[i] = v.ContainsKey(i) ? v[i] + 1 : 1;
            }
            else if(consonants.Contains(i))
            {
                c[i] = c.ContainsKey(i) ? c[i] + 1 : 1;
            }
        }
        int mv = v.Count > 0 ? v.Values.Max() : 0;
        int mc = c.Count > 0 ? c.Values.Max() : 0;
        return mv + mc;
    }
}