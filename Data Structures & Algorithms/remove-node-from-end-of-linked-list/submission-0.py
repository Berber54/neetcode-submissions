# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head
        for i in range(n):
            r = r.next

        while True:
            if r == None:
                l.next = l.next.next
                break
            l = l.next
            r = r.next

        return dummy.next