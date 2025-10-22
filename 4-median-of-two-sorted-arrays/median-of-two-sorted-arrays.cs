public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        List<int> combo = new List<int> (nums1);
        combo.AddRange(nums2);
        combo.Sort();
        int n = combo.Count();
        if(n%2==0)
        {
            return (combo[n/2-1]+combo[n/2])/2.0f;
        }
        else
        {
            return combo[n/2];
        }
    }
}