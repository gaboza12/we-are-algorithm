#include <bits/stdc++.h>

using namespace std;

int n;

map<string, int> m;

bool flag = false;

int ans = 0;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		string s1, s2;

		cin >> s1 >> s2;

		if (s1 == "ChongChong" || s2 == "ChongChong")
		{
			flag = true;
			m[s1] = 1;
			m[s2] = 1;
		}

		if (flag)
		{
			if (m[s1] == 1 || m[s2] == 1)
			{
				m[s1] = 1;
				m[s2] = 1;
			}
		}
	}

	for (auto nxt : m)
	{
		if (nxt.second == 1)
			ans++;
	}

	cout << ans;

	return 0;
}