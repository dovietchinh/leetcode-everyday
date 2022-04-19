// https://leetcode.com/problems/reverse-integer/

#include <string>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution{
	public:
		int reverse(int x){
			string temp = std::to_string(x);
			cout << x << ":" << temp << endl;
			std::reverse(temp.begin(),temp.end());
			try{
				if(x>0){	return std::stoi(temp);}
				else{return -std::stoi(temp);}
			}
			catch(){
				return 0;
			}
		}
};

int main(int argc,char** argv){
	Solution solution;
	vector<int> x = {123,-123,123};
	for(auto i:x){
		cout << solution.reverse(i) << endl;
	}
	return EXIT_SUCCESS;
}
