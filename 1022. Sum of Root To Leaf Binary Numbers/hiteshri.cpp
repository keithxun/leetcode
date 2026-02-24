#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

int dfsTraversal(TreeNode* root, int currSum){

    currSum = currSum*2 + root->val;
    if(root->left == NULL && root->right == NULL) return currSum;

    int left = 0, right = 0;

    if(root->left != NULL) left = dfsTraversal(root->left, currSum);
    if(root->right != NULL) right = dfsTraversal(root->right, currSum);

    return left + right;
}

int sumRootToLeaf(TreeNode* root){

    return dfsTraversal(root, 0);
}

