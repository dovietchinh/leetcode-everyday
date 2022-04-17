// https://github.com/dovietchinh/letcode-everyday/blob/master/source/problem14.cpp

#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

class Solution{
	public:
		string restoreString(string s, vector<int> indices){
			vector<pair<char,int>> list_s;
			for(int i=0;i<s.size();i++){
				char c = s.at(i);
				int temp = indices[i];
				list_s.push_back(make_pair(c,temp));
			}
			std::sort(list_s.begin(),list_s.end(), [](pair<char,int> a, pair<char,int> b){return a.second < b.second;});
			char p[s.size()+1] ;
			for(int i=0;i<s.size();i++){
				p[i] = list_s[i].first;
			}
			p[s.size()] = 0;
			return p;
		}


};

int main(int argc, char** argv){
	string s = "abcde";
	vector<int> indices{3,2,1,5,4};
	Solution solution;
	string result = solution.restoreString(s,indices);
	cout << result << endl;
	return EXIT_SUCCESS;
}
