class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxy=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i]==s[j]:
                    maxy=max(maxy,j-i)
        return maxy-1