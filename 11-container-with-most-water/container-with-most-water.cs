public class Solution {
    public int MaxArea(int[] height) {
        int cap = 0;
        int i = 0, j = height.Length-1;
        while(j>i)
        {
            int s = j-i;
            cap = Math.Max(cap, s*Math.Min(height[i], height[j]));
            if(height[i]>height[j]){
                j--;
            }
            else{
                i++;
            }
        }
        return cap;
    }
}