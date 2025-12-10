# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head.next
        dummy=ListNode(0)
        tail=dummy;s=0
        while curr:
            if curr.val!=0:
                s+=curr.val
            else:
                tail.next=ListNode(s)
                tail=tail.next
                s=0
            curr=curr.next
        return dummy.next