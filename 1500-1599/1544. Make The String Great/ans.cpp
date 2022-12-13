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
    string makeGood(string s) {
        vector<char> st;

        for (char c: s) {
            if (st.empty()) {
                st.push_back(c);
            } else {
                if (abs(st.back() - c) == 32) {
                    st.pop_back();
                } else st.push_back(c);
            }
        }

        return string(st.begin(), st.end());
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