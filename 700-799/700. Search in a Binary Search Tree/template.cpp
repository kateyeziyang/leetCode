#include <string>
#include <vector>
#include <set>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    struct TreeNode {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode() : val(0), left(nullptr), right(nullptr) {}
        TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
        TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
    };

    TreeNode* searchBST(TreeNode* root, int val) {
        TreeNode* p = root;
        while (p) {
            if (p->val == val) return p;
            if (p->val < val) {
                p = p->right;
                continue;
            }
            p = p-> left;
        }
        return NULL;
    }
};

// int main() {
//     Solution mysol;
//     int result;
//     vector<int>

//     cout << result << endl;
//     assert();

//     cout << "Finished.\n";

//     return 0;
// }