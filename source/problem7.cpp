#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
bool cmp(pair<string, int>& a,
         pair<string, int>& b)
{
    return a.second < b.second;
}
  
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* x, *z;
        vector<pair<int, ListNode*> > A;
        for(ListNode* p=list1;p!=NULL;p=p->next){
            A.push_back(p->val,p->next);
        }
        sort(A.begin(),A.end(),cmp);
        z = A[0].second;
        for(auto i : A){
            x->val = i.first;
            x->next = i.second;
            x = x->next;
        }
        return z;

    }
};

int main(int argc,char** argv){
    ListNode *l1;
    l1 -> next = new ListNode;
    l1 -> val = 3;
    l1 = l1->next;
    l1 -> val = 2;
    ListNode *l2;
    l2 -> next = new ListNode;
    l2 -> val = 3;
    l2 = l2->next;
    l2 -> val = 2;
    Solution solution;
    ListNode *l3 = solution.mergeTwoLists(l1,l2);
    for(ListNode* p =l3;p!=NULL;p=p->next){
        cout << p->val << endl;
    }
    return EXIT_SUCCESS;
    
}