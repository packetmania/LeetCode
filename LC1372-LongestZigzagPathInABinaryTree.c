/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxLen = 0;

// direction: 0 - left, 1 - right
void dfs(struct TreeNode* node, int direction, int length) {
    if (!node) return;

    if (length > maxLen) maxLen = length;

    // If we go the same direction, reset length to 1,
    // else increment length.
    dfs(node->left, 0, direction == 0 ? 1 : length + 1);
    dfs(node->right, 1, direction == 1 ? 1 : length + 1);
}

int longestZigZag(struct TreeNode* root) {
    maxLen = 0;
    // Start from root, go left or right
    dfs(root->left, 0, 1);
    dfs(root->right, 1, 1);
    return maxLen;
}


// DFS solution
// Time: O(n)
// Space: O(h) h is the height of the tree