#include <string>
#include <vector>
#include <set>
#include <cassert>
#include <iostream>
#include <unordered_map>

using namespace std;

// Runtime: 8 ms, faster than 33.94% of C++ online submissions for Kth Smallest Instructions.
// Memory Usage: 15.4 MB, less than 43.58% of C++ online submissions for Kth Smallest Instructions.
class Solution {
public:
    // int cannot hold ...
    // int fact(int x) {
    //     // if (x < 0) return 0;
    //     if (x <= 1) return 1;
    //     return x * fact(x-1);
    // }

    size_t comb(int n, int r) {
        size_t ans = 1;
        for (int i = 1, j = n - r + 1; i <= r; ++i, ++j) ans = ans * j / i;
        return ans;
    }

    string kthSmallestPath(vector<int>& destination, int k) {
        int v = destination[0], h = destination[1];
        size_t numRanks = comb(v+h, v);
        // int numRanks = fact(v+h) / fact(v) / fact(h);
        if (k < 1 || k > numRanks) return "";
        string res = "";

        for (int i = 0; i < destination[0] + destination[1]; i++) {
            size_t nHRanks = numRanks * h / (v + h);
            if (k <= nHRanks) {
                res += "H";
                h--;
                if (!h) {
                    res += string(v, 'V');
                    break;
                }
                numRanks = nHRanks;
            } else {
                res += "V";
                v--;
                if (!v) {
                    res += string(h, 'H');
                    break;
                }
                k -= nHRanks;
                numRanks -= nHRanks;
            }
        }

        return res;
    }
};

int main() {
    Solution mysol;

    vector<int> destination = {2,3}; 
    // cout << mysol.kthSmallestPath(destination, 1) << endl;
    // assert(mysol.kthSmallestPath(destination, 1) == "HHHVV");
    // assert(mysol.kthSmallestPath(destination, 10) == "VVHHH");
    // assert(mysol.kthSmallestPath(destination, 9) == "VHVHH");

    // destination = {4,6}; 
    // assert(mysol.kthSmallestPath(destination, 1) == "HHHHHHVVVV");
    // assert(mysol.kthSmallestPath(destination, 210) == "VVVVHHHHHH");
    // assert(mysol.kthSmallestPath(destination, 209) == "VVVHVHHHHH");

    destination = {15,15}; 
    assert(mysol.kthSmallestPath(destination, 155117520) == "VVVVVVVVVVVVVVVHHHHHHHHHHHHHHH");

    cout << "Finished.\n";

    return 0;
}