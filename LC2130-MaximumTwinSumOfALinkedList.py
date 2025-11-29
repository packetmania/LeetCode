# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Calculate the maximum twin sum
        max_twin_sum = 0
        first_half = head
        second_half = prev

        while second_half:
            twin_sum = first_half.val + second_half.val
            max_twin_sum = max(max_twin_sum, twin_sum)
            first_half = first_half.next
            second_half = second_half.next

        return max_twin_sum