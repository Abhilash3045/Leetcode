class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        alice=0;bob=0
        piles.sort()
        i=len(piles)-1
        while i>=0:
            alice+=piles[i]
            bob+=piles[i-1]
            i-=2
        return alice>bob
