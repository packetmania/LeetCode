/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head) {
    struct ListNode *curr_odd;
    struct ListNode *curr_even;
    struct ListNode *first_even;

    if (!head) {
        return NULL;
    }

    curr_odd = head;
    first_even = curr_even = head->next;

    while (curr_even && curr_even->next) {
        // Link odd nodes together
        curr_odd->next = curr_even->next;
        curr_odd = curr_odd->next;
        // Link even nodes together
        curr_even->next = curr_odd->next;
        curr_even = curr_even->next;
    }

    // Link the end of odd list to the head of even list
    curr_odd->next = first_even;

    return head;
}


// Time Complexity: O(n)
// Space Complexity: O(1)