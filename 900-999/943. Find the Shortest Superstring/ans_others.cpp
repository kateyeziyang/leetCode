#include <string>
#include <vector>
#include <set>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <numeric>

using namespace std;

// from https://leetcode.com/problems/find-the-shortest-superstring/discuss/199029/Rewrite-the-official-solution-in-C%2B%2B
class Solution {
public:
    string shortestSuperstring(vector<string>& A) {
        int n = A.size();
        
        vector<vector<int>> overlaps(n, vector<int>(n));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int m = min(A[i].size(), A[j].size());
                for (int k = m; k >= 0; --k) {
                    if (A[i].substr(A[i].size() - k) == A[j].substr(0, k)) {
                        overlaps[i][j] = k;
                        break;
                    }
                }
            }
        }
  
        // dp[mask][i] = most overlap with mask, ending with ith element (ith 也包含在了mask里面)
        vector<vector<int>> dp(1<<n, vector<int>(n, 0));
        vector<vector<int>> parent(1<<n, vector<int>(n, -1));
        
        for (int mask = 0; mask < (1<<n); ++mask) {
            //以下循环是为了计算dp[mask][bit]
            for (int bit = 0; bit < n; ++bit) {
                if (((mask>>bit)&1) > 0) {//说明bit位在mask里面，此时dp[mask][bit]才有意义
                    int pmask = mask^(1<<bit);//这一步是为了把bit位从mask里面去掉
                    if (pmask == 0) continue;//如果mask里面只有一个词，那么跳过
                    for (int i = 0; i < n; ++i) {
                        if (((pmask>>i)&1) > 0) {//如果pmask里面包含了第i位，那么计算以i结尾的pmask，再接上bit位
                            int val = dp[pmask][i] + overlaps[i][bit];
                            if (val > dp[mask][bit]) {//如果新算出来的overlap比较大，那么替换原有overlap
                                dp[mask][bit] = val;
                                parent[mask][bit] = i;//保存这种情况下以bit结尾的前一个词。
                            }
                        }
                    }
                }
            }
        }
        
        vector<int> perm;
        vector<bool> seen(n);
        int mask = (1<<n) - 1;
        
        int p = 0;//先计算出答案的最后一个单词
        for (int i = 0; i < n; ++i) {
            if (dp[(1<<n) - 1][i] > dp[(1<<n) - 1][p]) {
                p = i;
            }
        }
        
        //通过parent数组依次回溯出最后一个单词是p这种情况下，前面所有的排列
        while (p != -1) {
            perm.push_back(p);
            seen[p] = true;
            int p2 = parent[mask][p];
            mask ^= (1<<p);//从mask里面移走p
            p = p2;
        }
        
        //由于回溯出来的是反的，倒一下
        reverse(perm.begin(), perm.end());
        
        //加上没有出现的单词
        for (int i = 0; i < n; ++i) {
            if (!seen[i]) {
                perm.push_back(i);
            }
        }
        
        string ans = A[perm[0]];
        for (int i = 1; i < n; ++i) {
            int overlap = overlaps[perm[i - 1]][perm[i]];
            ans += A[perm[i]].substr(overlap);
        }
        
        return ans;
        
    }
};

int main() {
    Solution mysol;
    int result;

    // result = mysol.getOverlap("apeigneaz", "gneazpwoe");
    // cout << result << endl;
    // assert(result == 5);

    vector<string> words = {"alex","loves","leetcode"};
    string res = mysol.shortestSuperstring(words);
    cout << res << endl;
    assert(res == "alexlovesleetcode");

    words = {"catg","ctaagt","gcta","ttca","atgcatc"};
    res = mysol.shortestSuperstring(words);
    cout << res << endl;
    assert(res == "gctaagttcatgcatc");

    cout << "Finished.\n";

    return 0;
}