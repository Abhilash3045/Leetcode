class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans=-1;h={}
        for i in range(len(s)):
            if s[i] in h.keys():
                ans=max(ans, i-h[s[i]]-1)
            else:
                h[s[i]]=i
        return ans