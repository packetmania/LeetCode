/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    struct ListNode* fast;
    struct ListNode* slow;
    struct ListNode* prev;

    if (!head->next) {
        free(head);
        return NULL;
    }
    fast = slow = head;

    while (fast && fast->next) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }

    /* delete the slow node as the middle node */
    prev->next = slow->next;
    free(slow);

    return head;
}


// Simple C solution with fast/slow pointers. Note here needs a previous
// pointer (prev) to maintain the linked list after deleting the middle node.
// Time Complexity: O(n)
// Space Complexity: O(1)