public class Solution {
    public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
        List<bool> res = new List<bool>();
        int m = candies.Max();
        foreach(int i in candies){
            if(i+extraCandies>=m){
                res.Add(true);
            }
            else{
                res.Add(false);
            }
        }
        return res;
    }
}