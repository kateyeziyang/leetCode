#include <string>
#include <vector>
#include <set>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <numeric>

using namespace std;

// Dynamic programming.
// Sort functions comes from https://stackoverflow.com/questions/17074324/how-can-i-sort-two-vectors-in-the-same-way-with-criteria-that-uses-only-one-of?noredirect=1&lq=1
// Runtime: 96 ms, faster than 90.71% of C++ online submissions for Maximum Profit in Job Scheduling.
// Memory Usage: 48.1 MB, less than 86.84% of C++ online submissions for Maximum Profit in Job Scheduling.
class Solution {
public:
    template <typename T, typename Compare>
    std::vector<std::size_t> sort_permutation(
        const std::vector<T>& vec,
        Compare compare)
    {
        std::vector<std::size_t> p(vec.size());
        std::iota(p.begin(), p.end(), 0);
        std::sort(p.begin(), p.end(),
            [&](std::size_t i, std::size_t j){ return compare(vec[i], vec[j]); });
        return p;
    }

    template <typename T>
    std::vector<T> apply_permutation(
        const std::vector<T>& vec,
        const std::vector<std::size_t>& p)
    {
        std::vector<T> sorted_vec(vec.size());
        std::transform(p.begin(), p.end(), sorted_vec.begin(),
            [&](std::size_t i){ return vec[i]; });
        return sorted_vec;
    }

    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        auto p = sort_permutation(startTime, std::less<int>());

        vector<int> stT = apply_permutation(startTime, p);
        vector<int> edT = apply_permutation(endTime, p);
        vector<int> pf = apply_permutation(profit, p);

        int len = profit.size();
        int maxProfitI[len];
        maxProfitI[len-1] = pf[len-1];

        for (int i = len-2; i>=0; i--) {
            int profitWithI = pf[i];
            for (int j = i+1; j<len; j++) {
                if (stT[j] >= edT[i]) {
                    profitWithI += maxProfitI[j];
                    break;
                }
            }
            maxProfitI[i] = profitWithI > maxProfitI[i+1] ? profitWithI : maxProfitI[i+1];
        }

        return maxProfitI[0];
    }
};

int main() {
    Solution mysol;

    vector<int> startTime = {1,2,3,3}, endTime = {3,4,5,6}, profit = {50,10,40,70};
    int result;
    // result = mysol.jobScheduling(startTime, endTime, profit);
    // assert(result == 120);

    // startTime = {1,2,3,4,6}, endTime = {3,5,10,6,9}, profit = {20,20,100,70,60};
    // result = mysol.jobScheduling(startTime, endTime, profit);
    // assert(result == 150);

    // startTime = {1,1,1}, endTime = {2,3,4}, profit = {5,6,4};
    // result = mysol.jobScheduling(startTime, endTime, profit);
    // assert(result == 6);

    startTime = {6,15,7,11,1,3,16,2}, endTime = {19,18,19,16,10,8,19,8}, profit = {2,9,1,19,5,7,3,19};
    result = mysol.jobScheduling(startTime, endTime, profit);
    assert(result == 41);

    cout << "Finished.\n";

    return 0;
}