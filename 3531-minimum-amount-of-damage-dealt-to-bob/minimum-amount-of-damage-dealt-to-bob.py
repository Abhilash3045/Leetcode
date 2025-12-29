class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        enemies=[]
        for d, h in zip(damage, health):
            hits=(h+power-1)//power
            enemies.append((d,hits))
        enemies.sort(key=lambda x : -x[0]/x[1])
        hpl=0
        td=sum(damage)
        for d, hits in enemies:
            hpl+=(td)*hits
            td-=d
        return hpl