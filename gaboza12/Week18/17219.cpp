#include <bits/stdc++.h>

using namespace std;

int n, m;

map<string, string> mp;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		string address, password;

		cin >> address >> password;

		mp[address] = password;
	}

	for (int i = 0; i < m; i++)
	{
		string s;

		cin >> s;

		cout << mp[s] << "\n";
	}

	return 0;
}