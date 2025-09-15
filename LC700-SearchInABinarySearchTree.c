/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* searchBST(struct TreeNode* root, int val) {
    struct TreeNode* current = root;

    while (current) {
        if (val < current->val) {
            current = current->left;
        } else if (val > current->val) {
            current = current->right;
        } else {
            return current;
        }
    }

    return NULL;
}