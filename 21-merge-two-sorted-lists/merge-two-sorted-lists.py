# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        combo=[]
        curr=list1
        while curr:
            combo.append(curr.val)
            curr=curr.next
        curr=list2
        while curr:
            combo.append(curr.val)
            curr=curr.next
        combo.sort()
        dummy=ListNode(0)
        curr=dummy
        for i in combo:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next