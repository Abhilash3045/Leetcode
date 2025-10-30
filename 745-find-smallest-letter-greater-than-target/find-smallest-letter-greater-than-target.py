class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        a="abcdefghijklmnopqrstuvwxyz"
        m=a.index(target)
        for i in letters:
            if a.index(i)>m:
                return i
        return letters[0]