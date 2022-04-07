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
        int k =0;
        while(true){
            k++;
            if(x/pow(10,k)<1){
                break;
            }
            
        }
        int total =0;
        for(int i=1;i<=k;i++){
            int temp = pow(10,i);
            temp = x % temp;
            temp =  temp / pow(10,i-1);
            total += temp * pow(10,k-i);
        }
        return (total - x) ==0;
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