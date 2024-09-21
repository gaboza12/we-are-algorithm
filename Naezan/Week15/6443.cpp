#include <bits/stdc++.h>

using namespace std;

int N, S;

string s;
string ans;

vector<bool> check;
unordered_set<string> cached;

void calc(int n)
{
	if (n == s.size())
	{
		cout << ans << '\n';
		return;
	}

	for (int i = 0; i < s.size(); ++i)
	{
		if (!check[i])
		{
			check[i] = true;
			ans[n] = s[i];

			//중복체크
			string temp = ans.substr(0, n + 1);
			if (cached.count(temp) == 0)
			{
				cached.emplace(temp);
				calc(n + 1);
			}
			check[i] = false;
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N;

	for (int i = 0; i < N; ++i)
	{
		s.clear();
		ans.clear();
		check.clear();
		cached.clear();

		cin >> s;

		ans.resize(s.size());
		check.resize(s.size());

		sort(s.begin(), s.end());

		calc(0);
	}

	return 0;
}