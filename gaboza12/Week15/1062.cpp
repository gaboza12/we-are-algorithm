#include <bits/stdc++.h>

using namespace std;

int n, k;

bool alpha[26];

vector<string> v;
int ans = 0;

int func()
{
	int cnt = 0;

	for (int i = 0; i < v.size(); i++)
	{
		bool flag = true;

		for (int j = 0; j < v[i].size(); j++)
		{
			if (!alpha[v[i][j] - 'a'])
			{
				flag = false;
				break;
			}
		}

		if (flag)
		{
			cnt++;
		}
	}

	return cnt;
}

void dfs(int idx, int cnt)
{
	if (cnt == k)
	{
		ans = max(ans, func());
		return;
	}

	for (int i = idx; i < 26; i++)
	{
		if (alpha[i])
			continue;

		alpha[i] = true;
		dfs(i, cnt + 1);
		alpha[i] = false;
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> k;

	for (int i = 0; i < n; i++)
	{
		string temp;

		cin >> temp;

		v.push_back(temp);
	}

	if (k < 5)
	{
		cout << 0;
		return 0;
	}

	//최소 5개를 가르쳐야함
	k -= 5;

	alpha['a' - 'a'] = true;
	alpha['n' - 'a'] = true;
	alpha['t' - 'a'] = true;
	alpha['i' - 'a'] = true;
	alpha['c' - 'a'] = true;

	dfs(0, 0);

	cout << ans;

	return 0;
}