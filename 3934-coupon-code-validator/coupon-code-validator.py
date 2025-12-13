class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ele=[]; gro=[]; pha=[]; rest=[]
        
        for i in range(len(isActive)):
            if not code[i]:
                continue
            if isActive[i] and all(j.isalnum() or j == '_' for j in code[i]):
                if businessLine[i] == "electronics":
                    ele.append(code[i])
                elif businessLine[i] == "grocery":
                    gro.append(code[i])
                elif businessLine[i] == "pharmacy":
                    pha.append(code[i])
                elif businessLine[i] == "restaurant":
                    rest.append(code[i])
        ele.sort()
        gro.sort()
        pha.sort()
        rest.sort()
        return ele+gro+pha+rest