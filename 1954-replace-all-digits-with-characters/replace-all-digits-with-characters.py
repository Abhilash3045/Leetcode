alphabets = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
def shift(pr , ab):
    ab = int(ab)
    idx = alphabets.index(pr)
    idx += ab
    return alphabets[idx]
class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        new = ""
        for i in range(len(s)):
            if s[i] in alphabets:
                new += s[i]
            elif s[i] in numbers:
                new += (shift(s[i-1], s[i]))
        return new