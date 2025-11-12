class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        b=sorted(score, reverse=True)
        n=len(b)
        r=[""]*n
        for i in range(n):
            id=score.index(b[i])
            if i==0:
                r[id]="Gold Medal"
            elif i==1:
                r[id]="Silver Medal"
            elif i==2:
                r[id]="Bronze Medal"
            else:
                r[id]=str(i+1)
        return r