class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left,right=0,len(letters)-1
        res=""
        while left<=right:
            mid=(left+right)//2
            if ord(letters[mid])>ord(target):
                res=letters[mid]
                right=mid-1
            else:
                left=mid+1
        return res if res else letters[0]