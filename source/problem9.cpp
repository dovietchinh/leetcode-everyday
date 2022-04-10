#include <iostream>
using namespace std;

struct TreeNode {
     int val;
     struct TreeNode left;
     struct TreeNode right;
     struct TreeNode(int x) { val = x; }
};

class Solution {
  public :
  bool isSameTree(TreeNode *p, TreeNode *q) {
    // p and q are both null
    if (p == NULL && q == NULL) return true;
    // one of p and q is null
    if (q == NULL || p == NULL) return false;
    if (p->val != q->val) return false;
    return isSameTree(p->right, q->right) &&
            isSameTree(p->left, q->left);
  }
};

int main(int argc, char**argv){
  TreeNode *p, *q;
  p = new TreeNode;
  p-> val = 10;
  p-> right = new TreeNode;
  p-> left = new TreeNode;
  p->right->val = 5;
  p->left->val = 5;
  
  q = new TreeNode;
  q-> val = 12;
  q-> right = new TreeNode;
  q-> left = new TreeNode;
  q->right->val = 7;
  q->left->val = 7;
  Solution solution;
  bool x = solution.isSameTree(p,q);
  cout << x <<endl;
  return EXIT_SUCCESS;
}