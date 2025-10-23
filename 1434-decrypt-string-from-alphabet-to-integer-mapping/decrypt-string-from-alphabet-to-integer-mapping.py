class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = ""
        i = 0
        alp = '0abcdefghijklmnopqrstuvwxyz'
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                a = int(s[i:i+2])
                m += alp[a]
                i += 3
            else:
                a = int(s[i])
                m += alp[a]
                i += 1
        return m

        