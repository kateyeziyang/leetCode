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
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int n = nums.size();
        return setNode(0,n-1,nums);
    }

    TreeNode* setNode(int l, int r, vector<int>& nums) {
        if (l>r) return NULL;
        int m = l+(r-l)/2;
        TreeNode* cur = new TreeNode(nums[m]);
        cur->left = setNode(l,m-1,nums);
        cur->right = setNode(m+1,r,nums);
        return cur;
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