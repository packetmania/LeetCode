/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    if (!root || root == p || root == q) {
        return root;
    }

    struct TreeNode* left;
    struct TreeNode* right;

    left = lowestCommonAncestor(root->left, p, q);
    right = lowestCommonAncestor(root->right, p, q);

    if (left && right) {
        return root;  //* root is the LCA
    }

    return left ? left : right;
}

// DFS approach to find the lowest common ancestor (LCA) of two nodes in a binary tree.
// The function recursively traverses the tree and checks for the presence of nodes p and q.
// If both nodes are found in different subtrees of a node, that node is the LCA.

// Time Complexity: O(N) where N is the number of nodes in the binary tree.
// Space Complexity: O(H) where H is the height of the binary tree.
// This space is used to store the recursion stack.

// Note: This implementation assumes that both p and q are present in the tree.