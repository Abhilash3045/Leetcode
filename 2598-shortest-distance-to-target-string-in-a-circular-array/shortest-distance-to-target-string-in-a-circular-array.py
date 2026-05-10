class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        n=len(words)
        ans=float('inf')
        for i in range(n):
            if words[i]==target:
                d=abs(i-startIndex)
                ans=min(ans,d,n-d)
        return ans