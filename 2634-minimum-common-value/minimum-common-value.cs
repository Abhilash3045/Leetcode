public class Solution
{
    public int GetCommon(int[] nums1, int[] nums2)
    {
        if (nums1.Length > nums2.Length)
        {
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }

        foreach (int x in nums1)
        {
            int l = 0;
            int r = nums2.Length - 1;

            while (l <= r)
            {
                int mid = (l + r) / 2;

                if (nums2[mid] == x)
                {
                    return x;
                }
                else if (nums2[mid] > x)
                {
                    r = mid - 1;
                }
                else
                {
                    l = mid + 1;
                }
            }
        }

        return -1;
    }
}