public class Solution {
    public int CanBeTypedWords(string text, string brokenLetters) {
        string[] words = text.Split(' ');
        int count = 0;
        foreach(string word in words)
        {
            bool ans = false;
            foreach(char letter in word)
            {
                if(brokenLetters.Contains(letter))
                {
                    ans = true;
                    break;
                }
            }
            if(!ans)
            {
                count++;
            }
        }
        return count;
    }
}