class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        ans=[]
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(s, c):
            if len(s)==len(digits):
                ans.append(s)
                return
            for letter in phone[digits[c]]:
                backtrack(s+letter, c+1)
        backtrack("", 0)
        return ans