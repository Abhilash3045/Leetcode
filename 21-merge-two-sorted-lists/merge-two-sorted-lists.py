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
        # combo=[]
        # curr=list1
        # while curr:
        #     combo.append(curr.val)
        #     curr=curr.next
        # curr=list2
        # while curr:
        #     combo.append(curr.val)
        #     curr=curr.next
        # combo.sort()
        # dummy=ListNode(0)
        # curr=dummy
        # for i in combo:
        #     curr.next=ListNode(i)
        #     curr=curr.next
        # return dummy.next
        
        dummy=ListNode()
        curr=dummy
        while list1 and list2:
            if list1.val<list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        if list1:
            curr.next=list1
        if list2:
            curr.next=list2
        return dummy.next