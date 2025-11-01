public class Solution {
    public string Interpret(string command) {
        int i = 0;
        string word = "";
        while(i < command.Length)
        {
            if(command[i]=='G')
            {
                word += "G";
                i++;
            }
            else if(i+1 < command.Length && command.Substring(i, 2)=="()")
            {
                word += "o";
                i+=2;
            }
            else if(i+3 < command.Length && command.Substring(i, 4)=="(al)")
            {
                word += "al";
                i += 4;
            }
            else
            {
                i++;
            }
        }
        return word;
    }
}