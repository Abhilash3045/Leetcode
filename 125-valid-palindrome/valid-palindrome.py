class Solution(object):
    def isPalindrome(self, s):
        ok = ''.join(i.lower() for i in s if i.isalnum())
        return ok == ok[::-1]
        
        