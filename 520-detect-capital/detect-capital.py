class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower():
            return True
        if word[0].isupper():
            if word[1:].isupper():
                return True
            elif word[1:].islower():
                return True
            else:
                return False
        if word[0].islower():
            if word[1:].islower():
                return True
            else:
                return False