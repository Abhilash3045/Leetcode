class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels="aeiou"
        consonants="bcdfghjklmnpqrstvwxyz"
        v, c = {}, {}
        for i in s:
            if i in vowels:
                v[i]=v.get(i, 0)+1
            elif i in consonants:
                c[i]=c.get(i, 0)+1
        mv=max(v.values()) if v else 0
        mc=max(c.values()) if c else 0
        return mv+mc