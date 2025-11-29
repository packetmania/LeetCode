/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    int leftdepth, rightdepth, max;

    if (root == NULL) {
        return 0;
    }

    leftdepth = maxDepth(root->left);
    rightdepth = maxDepth(root->right);

    if (leftdepth > rightdepth) {
        max = leftdepth;
    } else {
        max = rightdepth;
    }

    return 1 + max;
}


// DFS solution which goes through each node's left and right children recursively.
// Time complexity: O(n) where n is the number of nodes in the tree
// Space complexity: O(h) where h is the height of the tree (due to recursion stack)