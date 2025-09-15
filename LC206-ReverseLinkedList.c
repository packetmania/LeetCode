/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev = NULL;
    struct ListNode* nxt = NULL;
    struct ListNode* curr = head;

    while (curr) {
        nxt = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nxt;
    }
    return prev;
}


// Solution with 3 variable (prev, nxt, curr) and 4 steps per iteration in while loop.
// Time complexity: O(n) - We traverse the entire list once.
// Space complexity: O(1) - We use a constant amount of extra space.

