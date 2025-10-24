public class Solution {
    public string ReverseWords(string s) {
        List<string> word = s.Split(' ').ToList();
        List<string> words = new List<string>();
        foreach(string w in word)
        {
            string rev = new string(w.Reverse().ToArray());
            words.Add(rev);
        }
        return string.Join(" ", words);
    }
}