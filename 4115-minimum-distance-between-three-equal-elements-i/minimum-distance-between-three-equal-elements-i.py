class Solution(object):
    def minimumDistance(self, nums):
        def mind(a, b, c):
            return abs(a - b) + abs(a - c) + abs(b - c)
        h = {}
        res = float('inf')
        for i, num in enumerate(nums):
            if num not in h:
                h[num] = []
            h[num].append(i)
            if len(h[num]) >= 3:
                a, b, c = h[num][-3], h[num][-2], h[num][-1]
                res = min(res, mind(a, b, c))
        return res if res != float('inf') else -1