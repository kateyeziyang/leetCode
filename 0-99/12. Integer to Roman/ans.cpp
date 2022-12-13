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
    string intToRoman(int num) {
        // unordered_map<int, char> valToRoman ({{1000, "M"}, {500, "D"}, {100, "C"}, {50, "L"}, {10, "X"}, {5, "V"}, {1, "I"}});
        int vals[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        string ans = "";
        for (int i = 0; num != 0; i++) {
            while (num >= vals[i]) {
                num -= vals[i];
                ans += symbols[i];
            }
        }
        return ans;
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