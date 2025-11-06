# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h={}
        curr=head
        while curr:
            h[curr.val]=h.get(curr.val,0)+1
            curr=curr.next
        dummy=ListNode(0)
        curr=dummy
        while head:
            if h[head.val]==1:
                curr.next=ListNode(head.val)
                curr=curr.next
            head=head.next
        return dummy.next