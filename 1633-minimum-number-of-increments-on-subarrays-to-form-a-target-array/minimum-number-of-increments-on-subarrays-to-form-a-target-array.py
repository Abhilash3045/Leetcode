class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans,previous=0,0
        for i in target:
            if i>previous:
                ans+=i-previous
            previous=i
        return ans