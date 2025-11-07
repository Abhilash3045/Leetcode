class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a={}
        # for i in nums:
        #     if i not in a:
        #         a.update({i:1})
        #     else:
        #         a[i]+=1
        # for key, value in a.items():
        #     if value > len(nums)/2:
        #         return key
        c,d=0,0
        for i in nums:
            if c==0:
                d=i
            if i==d:
                c+=1
            else:
                c-=1
        return d