# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r=[]
        curr=head
        while curr:
            r.append(curr.val)
            curr=curr.next
        r.sort()
        dummy=ListNode()
        curr=dummy
        for i in r:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next