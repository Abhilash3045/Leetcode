public class Solution {
    public int LengthOfLastWord(string s) {
        string l = s.TrimEnd();
        string[] n = l.Split(' ');
        List<string> m = new List<string>(n);
        return m[m.Count-1].Length;
    }
}