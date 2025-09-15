/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int pairSum(struct ListNode* head) {
    /* Solution keypoints:
     *     1. Find the middle node - the starting point of the 2nd half.
     *     2. Reverse the 2nd half linked list
     *     3. Get the maximum twin sum with two pointers moving forward
     */

    /* 1. Find the middle node with fast and slow pointers */
    struct ListNode *slow = head;
    struct ListNode *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    /* 2. Reverse the 2nd half linked list */
    struct ListNode* prev = NULL;
    struct ListNode* curr = slow;  // start from the middle node
    struct ListNode* nextNode;

    while (curr) {
        nextNode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }

    /* 3. Get the maximum twin sum with two pointers moving forward */
    int maxSum = 0;
    struct ListNode* p1 = head;
    struct ListNode* p2 = prev;
    while (p2) {
        int sum = p1->val + p2->val;
        if (sum > maxSum) maxSum = sum;
        p1 = p1->next;
        p2 = p2->next;
    }

    return maxSum;
}


// Time complexity: O(n) - we traverse the linked list a constant number of times
// Space complexity: O(1) - we use a constant amount of extra space