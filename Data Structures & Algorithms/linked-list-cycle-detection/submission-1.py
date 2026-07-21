# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        past = {}

        while curr:
            if curr in past:
                if past[curr] == curr.next:
                    return True
            past[curr] = curr.next
            curr = curr.next
            
        return False