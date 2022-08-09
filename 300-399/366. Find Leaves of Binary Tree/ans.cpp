#include <string>
#include <vector>
#include <set>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <numeric>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
private:
    vector<vector<int>> solution;

public:
    int getHeight(TreeNode *root) {
        if (!root) {
            return -1;
        }
        int lHeight = getHeight(root->left);
        int rHeight = getHeight(root->right);

        int curHeight = max(lHeight,rHeight)+1;

        if (this->solution.size() == curHeight) {
            this->solution.push_back({});
        }

        this->solution[curHeight].push_back(root->val);

        return curHeight;
    }

    vector<vector<int>> findLeaves(TreeNode* root) {
        this->solution.clear();
        getHeight(root);

        return this->solution;
    }
};

int main() {
    Solution mysol;
    int result;
    vector<int> x;

    cout << result << endl;
    assert(true);

    cout << "Finished.\n";

    return 0;
}