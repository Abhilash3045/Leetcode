# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        length=0
        while temp:
            temp=temp.next
            length+=1
        dummy=ListNode(0, head)
        curr=dummy
        for i in range(length):
            if i==length-n:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return dummy.next