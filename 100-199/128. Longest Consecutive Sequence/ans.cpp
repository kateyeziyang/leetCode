#include <string>
#include <vector>
#include <unordered_set>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <numeric>
#include <stack>
#include <queue>

using namespace std;

class Solution {
public:

    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> vals(nums.begin(), nums.end());
        unordered_set<int> visited;
        int answer = 0;

        for (int val: vals) {
            if (visited.count(val) == 0) {
                visited.insert(val);
                int right = val, left = val;
                while (vals.count(right + 1) == 1) {
                    right += 1;
                    visited.insert(right);
                }
                while (vals.count(left - 1) == 1) {
                    left -= 1;
                    visited.insert(left);
                }
                answer = max(right - left + 1, answer);
            }
        }

        return answer;
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