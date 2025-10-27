class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        temp=0
        prev=0
        for row in bank:
            count=row.count('1')
            if count:
                temp+=prev*count
                prev=count
        return temp

        