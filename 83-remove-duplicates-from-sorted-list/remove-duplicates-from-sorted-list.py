# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=set()
        dummy=ListNode(0)
        curr=dummy
        while head:
            if head.val not in s:
                s.add(head.val)
                curr.next=ListNode(head.val)
                curr=curr.next
            head=head.next
        return dummy.next