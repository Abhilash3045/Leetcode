public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        List<int> mn = new List<int>();
        for(int i = 0 ; i<m; i++)
        {
            mn.Add(nums1[i]);
        }
        for(int i = 0 ; i<n ; i++)
        {
            mn.Add(nums2[i]);
        }
        mn.Sort();
        for(int i = 0 ; i < mn.Count ; i++)
        {
            nums1[i]=mn[i];
        }
    }
}