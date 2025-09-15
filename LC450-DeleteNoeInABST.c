/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* deleteNode(struct TreeNode* root, int key) {
    struct TreeNode *temp;

    if (!root) {
        return NULL;
    }

    // Traverse to find the node to delete
    if (key < root->val) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->val) {
        root->right = deleteNode(root->right, key);
    } else {
        // Node found, perform deletion
        // Case 1: Node with no child or one child
        if (!root->left) {
            temp = root->right;
            free(root);
            return temp;
        } else if (!root->right) {
            temp = root->left;
            free(root);
            return temp;
        }

        // Case 2: Node with two children
        // Find the in-order successor (smallest in the right subtree)
        temp = root->right;
        while (temp->left) {
            temp = temp->left;
        }

        // Copy the in-order successor's data to this node
        root->val = temp->val;

        // Delete the in-order successor
        root->right = deleteNode(root->right, temp->val);
    }

    return root;
}