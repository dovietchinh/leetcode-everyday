// https://github.com/dovietchinh/letcode-everyday/blob/master/source/problem10.cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Solution{
	public:
		
		int finalValueAfterOperations(vector<string> operations){
			int result = 0;
			for(auto i: operations){
				if(i.find("++")!=string::npos){
					result ++;
				}
				else result --;
			}
			return result;

		};

	
};

int main(int argc, char** argv){
	Solution solution;
	vector<string> x{"--X","X++","X++","++X"};
	int result = solution.finalValueAfterOperations(x);
	cout << result << endl;
	return EXIT_SUCCESS;
}
