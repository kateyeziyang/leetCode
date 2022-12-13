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
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());

        vector<int> selected;
        vector<vector<int>> result;
        backtrack(0, target, selected, candidates, result);
        return result;
    }

    void backtrack(int idx, int count, vector<int>& selected, vector<int>& candidates, vector<vector<int>>& result) {
        if (count == 0) {
            result.push_back(vector<int>(selected));
            return;
        }

        for (int i = idx; i < candidates.size(); ++i) {
            if (candidates[i] > count) {
                return;
            }
            selected.push_back(candidates[i]);
            backtrack(i, count - candidates[i], selected, candidates, result);
            selected.pop_back();
        }
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