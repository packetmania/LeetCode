# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            # Link odd nodes together
            odd.next = even.next
            odd = odd.next
            # Link even nodes together
            even.next = odd.next
            even = even.next

        odd.next = even_head  # Link the end of odd list to the head of even list
        return head