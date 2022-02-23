#include <string>
#include <vector>
#include <set>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <numeric>

using namespace std;

// https://leetcode.com/problems/zigzag-conversion/solution/
class Solution {
    public:
        string convert(string s, int numRows) {
            if (numRows==1) return s;
            vector<string> rows(min(numRows,int(s.size())));
            int curRow = 0;
            bool godown = false;

            for (char c: s) {
                rows[curRow] += c;
                if (curRow == 0 || curRow == numRows-1) godown = !godown;
                curRow += godown ? 1 : -1;
            }
            string ret;
            for (string row : rows) ret += row;
            return ret;
        }
};

int main() {
    Solution mysol;
    int result;
    vector<int> ;

    cout << result << endl;
    assert();

    cout << "Finished.\n";

    return 0;
}