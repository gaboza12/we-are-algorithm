#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n, h;

	cin >> n;
	
	stack<pair<int, int>> s; //인덱스, 높이

	for (int i = 0; i < n; i++)
	{
		cin >> h;
		
		while (!s.empty())
		{
			if (h < s.top().second)
			{
				cout << s.top().first << " ";
				break;
			}
			s.pop();
		}

		if (s.empty())
		{
			cout << "0 ";
		}
		
		s.push({ i + 1, h });
	}

	return 0;
}
