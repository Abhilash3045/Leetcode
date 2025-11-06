# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[]
        curr=head
        while curr:
            l.append(curr.val)
            curr=curr.next
        l[k-1],l[-k]=l[-k],l[k-1]
        dummy=ListNode(0,head)
        curr=dummy.next
        for i in l:
            curr.val=i
            curr=curr.next
        return dummy.next