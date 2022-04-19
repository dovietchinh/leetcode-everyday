#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution{
	public:
		string interpret(string command){
			command =  this->replace(command,"()","o");
			command = this->replace(command,"(al)","al");
			return command;
		};
		string replace(string x, string temp1, string temp2){
			size_t npos = x.find(temp1);
			if(npos==string::npos) return x;
			while(npos!=string::npos){
				x.replace(npos,temp1.length(),temp2);
				npos = x.find(temp1,npos+temp2.length());
			}
			return x;
		};

};

int main(int argc,char** argv){
	Solution solution;
	string command = "G()(al)";
	string command2 = "G()()()()(al)";

	cout << solution.interpret(command) << endl;
	cout << solution.interpret(command2) << endl;
	return EXIT_SUCCESS;

}
