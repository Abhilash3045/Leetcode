class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr=[]
        for i, n in enumerate(nums):
            total=0; x=n
            while x:
                total+=x%10
                x//=10
            arr.append((total, n, i))
        arr.sort()
        swaps=0
        for i in range(len(nums)): # almost backtracking kind
            while arr[i][2]!=i:
                j=arr[i][2]
                arr[i], arr[j] = arr[j], arr[i]
                swaps+=1

        return swaps