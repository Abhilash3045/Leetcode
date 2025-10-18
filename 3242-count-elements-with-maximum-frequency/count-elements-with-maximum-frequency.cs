public class Solution {
    public int MaxFrequencyElements(int[] nums) {
        Dictionary<int, int> md = new Dictionary<int, int>();
        foreach(int num in nums)
        {
            if(md.ContainsKey(num))
            {
                md[num]+=1;
            }
            else
            {
                md[num]=1;
            }
        }
        int x = 0;
        int mx = md.Values.Max();
        foreach(KeyValuePair<int, int> m in md)
        {
            if(m.Value==mx)
            {
                x+=m.Value;
            }
        }
        return x;
    }
}