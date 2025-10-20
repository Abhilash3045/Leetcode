public class Solution {
    public int FinalValueAfterOperations(string[] operations) {
        int x=0;
        foreach(string i in operations)
        {
            if(i=="++X" || i=="X++")
            {
                x++;
            }
            else if(i=="--X" || i=="X--")
            {
                x--;
            }
        }
        return x;
    }
}