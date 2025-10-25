public class Solution {
    public string TruncateSentence(string s, int k) {
        List<string> tr = s.Split(' ').ToList();
        List<string> trn = new List<string>();
        for(int i=0; i<k; i++) 
        {
            trn.Add(tr[i]);
        }
        return string.Join(' ', trn);
    }
}