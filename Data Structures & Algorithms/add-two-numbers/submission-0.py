# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        count1 = 0
        count2 = 0
        while l1:
            n1 += l1.val * 10 ** count1
            l1 = l1.next
            count1 += 1
        
        while l2:
            n2 += l2.val *10 ** count2
            l2 = l2.next
            count2 += 1
        
        s = list(str(n1 + n2))
        prev = None
        for x in s:
            prev = ListNode(x, prev)
            
        return prev