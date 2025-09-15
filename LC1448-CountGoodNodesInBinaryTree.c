/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int dfs(struct TreeNode* currRoot, int currMax) {
    if (!currRoot) {
        return 0;
    }

    // Check if current node is a "good" node
    // A node is good if its value >= maximum value on path from root
    int goodNodes = 0;
    if (currRoot->val >= currMax) {
        goodNodes = 1;
        currMax = currRoot->val;   // Update currMax children
    }

    // Recursively count good nodes in left and right subtrees
    goodNodes += dfs(currRoot->left, currMax);
    goodNodes += dfs(currRoot->right, currMax);
    return goodNodes;
}

int goodNodes(struct TreeNode* root){
    return dfs(root, root ? root->val : 0);
}



// Simple dfs solution - counting good node of left/right subtree recursively with dfs calls.
// Time Complexity: O(N) where N is the number of nodes in the binary tree
// Space Complexity: O(H) where H is the height of the binary tree (due to recursion stack)

