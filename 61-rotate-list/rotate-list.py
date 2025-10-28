# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head

        length=1
        temp=head
        while temp.next:
            temp=temp.next
            length+=1
        temp.next=head      # made it as a circular linked list and we break it at end
        k%=length
        if k==0:
            temp.next=None
            return head
        new_last=head
        for _ in range(length-k-1):
            new_last=new_last.next
        new_head=new_last.next
        new_last.next=None
        return new_head