# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list has 0 or 1 nodes, a result is None.
        if head is None or head.next is None:
            return None

        fast = head
        slow = head
        prev = None

        # Move fast by 2 steps, slow by 1 step
        # prev tracks the node before slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # "Delete" the middle node (slow) by skipping it
        prev.next = slow.next

        # In Python, we don't need free(slow); garbage collector handles it
        return head
