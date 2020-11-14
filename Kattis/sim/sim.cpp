#include <iostream>

using namespace std;
int main()
{
	int n;
	cin >> n;
	string throwaway;
	getline(cin,throwaway);
	for(int i = 0;i<n;i++)
	{
		string line;
		getline(cin,line);
		int chars = line.length();
		string text = "";
		int index = 0;
		for(int j = 0;j<chars;j++)
		{
			char character = line[j];
			if(character == '<')
			{
				if(index>0)
				{
					text = text.substr(0,index-1) + text.substr(index,text.length());
					index--;
				}
			}
			else if(character == '[')
			{
				index = 0;
			}
			else if(character == ']')
			{
				index = text.length();
			}
			else
			{
				if(text.length()==0) 
				{
					text = text+character;
					index++;
				}
				else
				{
					text = text.substr(0,index) + character + text.substr(index,text.length());
					index++;
				}
			}
		}
		cout<<text<<endl;
	}
	return 0;
}
