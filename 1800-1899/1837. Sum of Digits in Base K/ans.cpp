#include "iostream"

using namespace std;

class Solution {
public:
    int sumBase(int n, int k) {
        int ans = 0;
        while (n) {
            ans += n%k;
            n /= k;
        }
        return ans;
    }
};

int main() {
    Solution sol;
    int r = sol.sumBase(106,6);
    cout << r << endl;
    r = sol.sumBase(10,10);
    cout << r << endl;
    r = sol.sumBase(64,8);
    cout << r << endl;
    return 0;
}