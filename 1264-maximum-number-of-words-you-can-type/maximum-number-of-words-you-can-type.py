class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split()
        c=0
        for t in text:
            if not any(ch in brokenLetters for ch in t):
                c+=1
        return c