# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=1
        temp=head
        while temp.next:
            length+=1
            temp=temp.next
        if length%2==1:
            avg=(length//2)
        elif length%2==0:
            avg=(length/2)
        dummy=ListNode(0)
        dummy.next=head
        curr=dummy
        i=0
        for i in range(length):
            if i==avg:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return dummy.next