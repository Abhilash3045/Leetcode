public class Solution {
    public bool DetectCapitalUse(string word) {
        if((word.All(char.IsUpper)) || (word.All(char.IsLower)))
        {
            return true;
        }
        if(char.IsUpper(word[0]))
        {
            if(word.Substring(1).All(char.IsUpper)){
                return true;
            }
            else if(word.Substring(1).All(char.IsLower)){
                return true;
            }
            else{
                return false;
            }
        }
        if(char.IsLower(word[0]))
        {
            if(word.Substring(0).All(char.IsLower))
            {
                return true;
            }
            else{
                return false;
            }
        }
        return false;
    }
}