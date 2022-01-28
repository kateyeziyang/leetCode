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
        int minFlipsMonoIncr(const std::string& S, int counter_one=0, int counter_flip=0) {
            for (auto ch: S) {
                if (ch == '1') {
                    ++counter_one;
                } else {
                    ++counter_flip;
                }
                counter_flip = min(counter_one,counter_flip);
            }
            return counter_flip;
        }
};

int main() {
    Solution mysol;
    int result = mysol.minFlipsMonoIncr("1100");

    cout << result << endl;
    assert(result==2);

    cout << "Finished.\n";

    return 0;
}