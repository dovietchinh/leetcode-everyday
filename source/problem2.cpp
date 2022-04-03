#include <cmath>
#include <iostream>
using namespace std;
struct ListNode{
    int val;
    ListNode *next;
    ListNode(){
        val = 0;
        next = NULL;
    }
    ListNode(int x) : val(x), next(nullptr) {};
    ListNode(int x, ListNode *next) : val(x), next(next) {};
};
class Solution {
public:
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
            ListNode *l3, *p;
            l3 = new ListNode;
            p = l3;
            int redendency = 0;
            while(l1||l2 and redendency!=0){
                int val = ((l1)?l1->val:0) + ((l2)?l2->val:0) + redendency; 
                l3->val = val%10;
                redendency = val / 10;
                l1 = (l1)?l1->next:NULL;
                l2 = (l2)?l2->next:NULL;
                if(l1||l2 and redendency!=0){
                    l3-> next = new ListNode;
                    l3 = l3 -> next;
                }
            }
            return p;
            
        }

};
int main(int argc, char ** argv){
    Solution x;
    ListNode *a = new ListNode[1];
    a->val = 1;
    a->next = new ListNode[1];
    a->next->val = 2;
    a->next->next = new ListNode[1];
    a->next->next->val = 3;

    ListNode *b = new ListNode[1];
    b->val = 4;
    b->next = new ListNode[1];
    b->next->val = 5;
    b->next->next = new ListNode[1];
    b->next->next->val = 6;
    b->next->next->next = new ListNode[1];
    b->next->next->next->val = 7;

    ListNode *c = x.addTwoNumbers(a,b);
    // cout << bool(a-> next) << endl;

    while(c){
        
        cout << c->val << endl;
        c = c->next;
    }
}