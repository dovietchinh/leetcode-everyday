/*
link : https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

*/
#include <iostream>
#include <string>
#include <sstream>
#include <bits/stdc++.h>
#include <vector>
#include <cmath>
using namespace std;
class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int revertedNumber = 0;
        while(x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }

        return x == revertedNumber || x == revertedNumber/10;
    }
};

int main(int argc, char **argv){
    Solution x;
    vector<string> vec;
    for(int i=1; i<argc; i++){
        vec.push_back((argv[i]));
    }
    for(auto element: vec){
        int temp;
        try{
            temp = stoi(element);
        }
        catch(int x){
            cout <<"error:"<<x << endl;
        }
        cout << x.isPalindrome(temp) << endl;
    }
    
    return EXIT_SUCCESS;
}