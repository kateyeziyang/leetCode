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
    string truncateSentence(string s, int k) {
        for (int i = 0; i<s.length(); i++) {
            if (s[i] == ' ') {
                k--;
                if (k == 0) return string(s, 0, i);
            }   
        }
        return s;
    }
};

int main() {
    Solution mysol;
    string result;
    string str = "Hello world my computer";

    result = mysol.truncateSentence(str, 1);
    cout << result << endl;
    assert(result=="Hello");

    result = mysol.truncateSentence(str, 3);
    assert(result=="Hello world my");

    result = mysol.truncateSentence(str, 4);
    assert(result=="Hello world my computer");

    cout << "Finished.\n";

    return 0;
}