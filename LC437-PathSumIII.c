/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

 // From the current node, count the paths which have matching target sum
int dfsFromNode(struct TreeNode* node, long long sum) {
    if (!node) return 0;

    int count = 0;
    if (node->val == sum) count++;

    count += dfsFromNode(node->left, sum - node->val);
    count += dfsFromNode(node->right, sum - node->val);

    return count;
}

// Traverse all tree nodes as the starting points
int pathSum(struct TreeNode* root, int targetSum) {
    if (!root) return 0;

    // Count the paths starting from root
    int res = dfsFromNode(root, targetSum);

    res += pathSum(root->left, targetSum);
    res += pathSum(root->right, targetSum);

    return res;
}


// DFS with prefix sum and dual recursions.
// Time complexity: O(N^2)
// Space complexity: O(H) where H is the height of the tree (due to recursion stack)