# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def combineLists(lists: list) -> list:
            r=[]
            for head in lists:
                curr=head
                while curr:
                    r.append(curr.val)
                    curr=curr.next
            return r
        
        combo=combineLists(lists)
        combo.sort()
        dummy=ListNode(0)
        curr=dummy
        for i in combo:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next
        