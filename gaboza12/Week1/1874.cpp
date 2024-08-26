#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	stack<int> s;
	vector<char> v;
	
	int n;
	
	cin>>n;
	
	int cnt=1;
	
	for(int i=0;i<n;i++)
	{
		int a;
		cin>>a;
		
		while(cnt<=a)
		{
			v.push_back('+');
			s.push(cnt);
			cnt++;
		}
		
		if(s.top()==a)
		{
			v.push_back('-');
			s.pop();
		}
		else
		{
			cout<<"NO\n";
			return 0;
		}
	}
	
	for(auto a : v)
	{
		cout<<a<<"\n";
	}

	return 0;
}
