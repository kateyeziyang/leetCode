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
// Runtime: 104 ms, faster than 83.18% of C++ online submissions for Maximum Profit in Job Scheduling.
// Memory Usage: 46.8 MB, less than 92.06% of C++ online submissions for Maximum Profit in Job Scheduling.
class Solution {
public:
    struct job {
        int st;
        int et;
        int prf;
    };

    static int compareByStart(job a, job b) {
        return a.st < b.st;
    }

    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int len = profit.size();
        vector<job> jobs(len);
        for (int i = 0; i < len; i++) { jobs[i].st = startTime[i]; jobs[i].et = endTime[i]; jobs[i].prf = profit[i]; }
        sort(jobs.begin(), jobs.end(), compareByStart);
        int maxProfitI[len];
        maxProfitI[len-1] = jobs[len-1].prf;


        for (int i = len-2; i>=0; i--) {
            int profitWithI = jobs[i].prf;
            for (int j = i+1; j<len; j++) {
                if (jobs[j].st >= jobs[i].et) {
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