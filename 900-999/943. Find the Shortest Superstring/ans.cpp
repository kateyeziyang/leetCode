#include <string>
#include <vector>
#include <set>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <numeric>

using namespace std;

// this solution timed out. anyway.
class Solution {
public:
    // return the max overlapping length between a's suffix and b's prefix
    int getOverlap(const string& a, const string& b) {
        int len = a.length() > b.length() ? b.length() : a.length();
        for (int i = a.length()-len; i<a.length(); i++) {
            if (a.substr(i) == b.substr(0, a.length()-i))
                return a.length()-i;
        }
        return 0;
    }

    string shortestSuperstring(vector<string>& words) {
        int len = words.size();
        int overlapLengths[len][len];
        for (int i = 0; i<len; i++) {
            for (int j = 0; j<len; j++) {
                if (i!=j)
                    overlapLengths[i][j] = getOverlap(words[i], words[j]);
                else
                    overlapLengths[i][j] = words[i].length();
            }
        }

        int count = 0, maxOverlapLen = 0;
        int seq[len], minseq[len];
        for (int i = 0; i<len; i++) minseq[i] = seq[i] = i;
        do {
            count = 0;
            for (int i = 0; i<len-1; i++) {
                count += overlapLengths[seq[i]][seq[i+1]];
            }
            if (count > maxOverlapLen) {
                maxOverlapLen = count;
                for (int i = 0; i<len; i++) minseq[i] = seq[i];
            }
        } while (next_permutation(seq, seq+len));

        string minStr = "";
        for (int i = 0; i<len-1; i++) {
            int first = minseq[i], second = minseq[i+1];
            minStr += words[first].substr(0, words[first].length()-overlapLengths[first][second]);
        }
        minStr += words[minseq[len-1]];

        return minStr;
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