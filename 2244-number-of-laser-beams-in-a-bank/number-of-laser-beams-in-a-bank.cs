public class Solution {
    public int NumberOfBeams(string[] bank) {
        int prev = 0, total = 0;
        foreach(string row in bank)
        {
            int count = 0;
            foreach(char cell in row)
            {
                count += cell & 1;
            }
            if(count > 0)
            {
                total += prev * count;
                prev = count;
            }
        }
        return total;
    }
}