// https://leetcode.com/problems/defanging-an-ip-address/

#include <string>
#include <iostream>
#include <vector>
using namespace std;

class Solution{
	public:
		string defangIPaddr(string address){
			return this->replace(address,".","[.]");
		};
		string replace(string x,string temp1,string temp2){
			size_t npos = x.find(temp1);
		//	if(npos==string::npos) return x;
			while(npos!=string::npos){
				x.replace(npos,temp1.length(),temp2);
				npos = x.find(temp1,npos+temp2.length());
			}
			return x;
		};
};
int main(int argc, char** argv){
	string test = "1.1.1.1";
	Solution solution;
	string result = solution.defangIPaddr(test);
	cout << result << endl;
	return EXIT_SUCCESS;
}
