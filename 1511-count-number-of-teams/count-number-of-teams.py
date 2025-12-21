class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating);ans=0
        for j in range(n):
            ls=ll=rs=rl=0
            for i in range(j):
                if rating[i]<rating[j]: ls+=1
                else:   ll+=1
            for k in range(j+1,n):
                if rating[k]>rating[j]: rl+=1
                else:   rs+=1
            ans+=ls*rl
            ans+=ll*rs
        return ans