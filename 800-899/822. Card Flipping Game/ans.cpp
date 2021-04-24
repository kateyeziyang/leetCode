#include <string>
#include <vector>
#include <set>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <numeric>

using namespace std;

// Idea: find min # k such that any card's front and back number are not k at the same time.
// Runtime: 16 ms, faster than 67.35% of C++ online submissions for Card Flipping Game.
// Memory Usage: 19.4 MB, less than 34.69% of C++ online submissions for Card Flipping Game.
class Solution {
public:
    int flipgame(vector<int>& fronts, vector<int>& backs) {
        int res = 2001;
        unordered_set<int> bothFB;
        for (int i = 0; i < fronts.size(); i++) {
            if (fronts[i] == backs[i]) bothFB.insert(fronts[i]);
        }
        for (int i = 0; i < fronts.size(); i++) {
            if (fronts[i] < res && !bothFB.count(fronts[i])) res = fronts[i];
            if (backs[i] < res && !bothFB.count(backs[i])) res = backs[i];
        }
        res = res == 2001 ? 0 : res;
        return res;
    }
};

int main() {
    Solution mysol;
    vector<int> fronts = {1,2,4,4,7}, backs = {1,3,4,1,3};
    int result;

    result = mysol.flipgame(fronts, backs);
    cout << "Your result is: " << result << endl;
    assert(result == 2);

    cout << "Finished.\n";

    return 0;
}