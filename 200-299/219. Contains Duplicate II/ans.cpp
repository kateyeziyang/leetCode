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
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, bool> window;
        for (int i = 0; i < min(k, (int) nums.size()); ++i) {
            if (window.count(nums[i]) > 0) {
                return true;
            }
            window[nums[i]] = true;
        }
        if (k >= (int) nums.size()) return false;
        for (int i = k; i < (int) nums.size(); ++i) {
            if (window.count(nums[i]) > 0) {
                return true;
            }
            window[nums[i]] = true;
            window.erase(nums[i-k]);
        }
        return false;
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