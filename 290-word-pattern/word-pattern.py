class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern,s=list(pattern),list(s.split())
        if len(pattern)!=len(s):
            return False
        else:
            h={}
            for i in range(len(s)):
                if pattern[i] not in h:
                    if s[i] in h.values():
                        return False
                    h[pattern[i]]=s[i]
                elif h[pattern[i]]!=s[i]:
                    return False
        return True
        