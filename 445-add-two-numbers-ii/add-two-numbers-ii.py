# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a=[]
        curr=l1
        while curr:
            a.append(curr.val)
            curr=curr.next
        b=[]
        curr=l2
        while curr:
            b.append(curr.val)
            curr=curr.next
        a=int("".join(map(str,a)))
        b=int("".join(map(str,b)))
        c=a+b
        c=list(map(int,str(c)))
        dummy=ListNode(0)
        curr=dummy
        for i in c:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next