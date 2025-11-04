class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n=len(nums)
        res=[]
        count=Counter(nums[:k])
        def xsum():
            freq=sorted(count.items(), key=lambda a: (-a[1],-a[0]))
            return sum(k*v for k,v in freq[:x])
        res.append(xsum())
        for i in range(k,n):
            left, right = nums[i-k], nums[i]
            count[left]-=1
            if count[left]==0:
                del count[left]
            count[right]+=1
            res.append(xsum())
        return res