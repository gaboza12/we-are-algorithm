#include <bits/stdc++.h>

using namespace std;

int n;

bool flag = false;
string ans = "";

void dfs(int cnt, string s)
{
	if (flag)
		return;

	for (int i = 1; i <= s.size() / 2; i++)
	{
		//나쁜수열 체크
		if (s.substr(s.size() - i, i) == s.substr(s.size() - (2 * i), i))
			return;
	}

	if (cnt == n)
	{
		ans = s;
		flag = true;
	}

	for (int i = 0; i < n; i++)
	{
		dfs(cnt + 1, s + "1");
		dfs(cnt + 1, s + "2");
		dfs(cnt + 1, s + "3");
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n;
	
	dfs(0, "");

	cout << ans;

	return 0;
}