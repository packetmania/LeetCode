# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # Save the next node
            curr.next = prev     # Reverse the link
            prev = curr          # Move prev to curr
            curr = nxt           # Move to the next node

        # prev now points to the new head of the reversed list
        return prev
