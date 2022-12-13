#include <string>
#include <vector>
#include <unordered_set>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    unordered_set<string> twoPowers;

    bool reorderedPowerOf2(int n) {
        twoPowers.clear();

        int a = 1;
        while (a <= INT_MAX / 2) {
            string astr = to_string(a);
            sort(astr.begin(), astr.end());
            twoPowers.insert(astr);
            a = a*2;
        }

        string nstr = to_string(n);
        sort(nstr.begin(), nstr.end());
        if (twoPowers.count(nstr) > 0) {
            return true;
        } else return false;
    }
};

int main() {
    Solution mysol;
    int result;
    vector<int> x;

    mysol.reorderedPowerOf2(1);

    cout << result << endl;
    assert(true);

    cout << "Finished.\n";

    return 0;
}