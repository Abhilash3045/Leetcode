# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        curr=head
        while curr:
            l.append(curr.val)
            curr=curr.next
        for i in range(0,len(l)-1,2):
            l[i],l[i+1]=l[i+1],l[i]
        dummy=ListNode(0,head)
        curr=dummy.next
        for i in l:
            curr.val=i
            curr=curr.next
        return dummy.next