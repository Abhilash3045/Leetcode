class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        h=[]
        temp=""
        for i in nums:
            temp+=str(i)
            binary=int(temp,2)
            if int(binary)%5==0:
                h.append(True)
            else:
                h.append(False)
        return h