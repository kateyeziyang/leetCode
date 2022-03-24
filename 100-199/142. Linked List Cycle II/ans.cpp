#include <string>
#include <vector>
#include <set>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <numeric>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (head==NULL) return NULL;
        ListNode *slow,*fast;
        slow = fast = head;
        while (fast!=NULL && fast->next!=NULL) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow==fast) {
                ListNode *third = head;
                while (third!=slow) {
                    third = third->next;
                    slow = slow->next;
                }
                return slow;
            }
        }
        return NULL;
    }
};

int main() {
    Solution mysol;
    int result;
    vector<int> ;

    cout << result << endl;
    assert(true);

    cout << "Finished.\n";

    return 0;
}