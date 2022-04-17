// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences

#include <string>
#include <iostream>
#include <vector>
using namespace std;

class Solution{
	public:
		int mostWordsFound(vector<string> s){
			int result = 0;
			for(auto i:s){
				vector<string> temp = this->split(i," ");
				if(temp.size()> result) result = temp.size();
			}
			return result;
		}
		vector<string> split(string x, string temp){
			vector<string> result;
			size_t npos = x.find(temp);
			size_t npos_old = npos;
			if(npos==string::npos){
				result.push_back(x);
			}
			while(npos!=string::npos){
				npos = x.find(temp);
				result.push_back(x.substr(0,npos));
				x = x.substr(npos+temp.length());
			}
			return result;
		}
};

int main(int argc, char** argv){
	Solution solution;
	vector<string> s{"alice and bob love leetcode", "i think so too", "this is great thanks very much"};
	int result = solution.mostWordsFound(s);
	cout << result << endl;
	return EXIT_SUCCESS;
}
