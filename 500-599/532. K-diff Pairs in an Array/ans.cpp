#include <vector>
#include <set>
#include <cassert>
#include <iostream>
#include <unordered_map>

using namespace std;

/* Using set, we can check if a value exists with constant time.
This is the advantage over searching the whole vector. */
/* Runtime: 16 ms, faster than 79.78% of C++ online submissions for K-diff Pairs in an Array.
Memory Usage: 13.3 MB, less than 47.12% of C++ online submissions for K-diff Pairs in an Array. */
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        if (k < 0) return 0;

        unordered_map<int, int> m; // the map store values and # times they appear
        for (int i : nums) m[i]++;

        int count = 0;
        for (const auto& it : m) {
            if (k > 0 && m.count(it.first + k)) count++;
            if (k == 0 && it.second >= 2) count++;
        }

        return count;
    }
};

int main() {
    Solution mysol;

    vector<int> nums = {3,1,4,1,5};
    int sol = mysol.findPairs(nums, 2);
    assert(sol==2);

    sol = mysol.findPairs(nums, 0);
    assert(sol==1);

    sol = mysol.findPairs(nums, 1);
    assert(sol==2);

    cout << "Finished.\n";

    return 0;
}

/* Runtime: 28 ms, faster than 26.20% of C++ online submissions for K-diff Pairs in an Array.
Memory Usage: 15.6 MB, less than 9.38% of C++ online submissions for K-diff Pairs in an Array. */
// class Solution {
// public:
//     int findPairs(vector<int>& nums, int k) {
//         if (k < 0) return 0;
//         set<int> leftIndices, visited;

//         for (int i : nums) {
//             if (visited.count(i - k)) {
//                 leftIndices.insert(i - k);
//             }
//             if (visited.count(i + k)) {
//                 leftIndices.insert(i);
//             }
//             visited.insert(i);
//         }

//         return leftIndices.size();
//     }
// };