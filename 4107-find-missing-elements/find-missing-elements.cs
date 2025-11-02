public class Solution {
    public IList<int> FindMissingElements(int[] nums) {
        List<int> res = new List<int>();
        int miny = nums.Min();
        int maxy = nums.Max();
        for(int i = miny+1; i < maxy; i++)
        {
            if(!nums.Contains(i))
            {
                res.Add(i);
            }
        }
        return res;
    }
}