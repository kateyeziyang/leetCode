#include <string>
#include <vector>
#include <set>
#include <cassert>
#include <stack>
#include <queue>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <numeric>

using namespace std;
struct TreeNode;
struct ListNode;

// ok, writing in cpp takes my hair
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if (root==NULL) {
            return true;
        }
        stack<pair<TreeNode*,int>> st;
        st.push({root,0});
        int minheight = -1;
        int maxheight = -1;
        while (!st.empty()) {
            auto p = st.top();
            st.pop();
            if (p.first->left) {
                st.push({p.first->left,1+p.second});
            } else {
                minheight = minheight==-1 ? p.second : min(minheight,p.second);
            }
            if (p.first->right) {
                st.push({p.first->right,1+p.second});
            }
            if (!p.first->left && !p.first->right) {
                minheight = minheight==-1 ? p.second : min(minheight,p.second);
                maxheight = maxheight==-1 ? p.second : max(maxheight,p.second);
                if (minheightmaxheight-minheight > 1) {
                    return false;
                }
            }
        }
        return true;
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

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};