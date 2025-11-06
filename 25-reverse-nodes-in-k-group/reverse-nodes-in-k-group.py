# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[]
        curr=head
        while curr:
            l.append(curr.val)
            curr=curr.next
        i,j=0,k
        m=[]
        while i<len(l):
            m+=l[i:j][::-1]
            i+=k
            j+=k
            if not j<=len(l):
                m+=l[i:]
                break
        dummy=ListNode(0,head)
        curr=dummy.next
        for i in m:
            curr.val=i
            curr=curr.next
        return dummy.next