public class Solution {
    public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
        List<bool> res = new List<bool>();
        int max = 0;
        foreach(int i in candies){
            if(i>max){
                max=i;
            }
        }
        foreach(int i in candies){
            if(i+extraCandies>=max){
                res.Add(true);
            }
            else{
                res.Add(false);
            }
        }
        return res;
    }
}