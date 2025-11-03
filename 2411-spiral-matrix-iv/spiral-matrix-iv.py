# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        List=[]
        curr=head
        while curr:
            List.append(curr.val)
            curr=curr.next
        extra=(m*n)-len(List)
        List+=[-1]*extra
        mat=[[0]*n for _ in range(m)]
        i=0
        top,bottom=0,m-1
        left,right=0,n-1
        while top<=bottom and left<=right:
            for x in range(left, right+1):          #top
                mat[top][x]=List[i]
                i+=1
            top+=1
            for x in range(top, bottom+1):          #right
                mat[x][right]=List[i]
                i+=1
            right-=1
            if top<=bottom:
                for x in range(right, left-1, -1):          #bottom
                    mat[bottom][x]=List[i]
                    i+=1
                bottom-=1
            if left<=right:
                for x in range(bottom, top-1, -1):          #left
                    mat[x][left]=List[i]
                    i+=1
                left+=1
        return mat