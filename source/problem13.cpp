// https://leetcode.com/problems/consecutive-characters/
#include <string>
#include <iostream>
#include <vector>
using namespace std;

class Solution{
	public:
		int maxPower(string x){
			int count_max = 1;
			int count = 0;
			char old = x[0];
			for(auto i:x){
				cout <<i << " " << old << " "<< count << endl;
				if(i==old){
					count += 1; 
					if(count>count_max){
						count_max = count;
					}
				}
				else{count = 1;}
				old = i;
			}
			return count_max;
		}
};


int main(int argc,char ** argv){
	string s = "abbcccddddeeeeedcba";
	Solution solution;
	int result = solution.maxPower(s);
	cout << result << endl;
	return EXIT_SUCCESS;
}
