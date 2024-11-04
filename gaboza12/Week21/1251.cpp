#include <bits/stdc++.h>

using namespace std;

string s;
vector<string> vec;
string ans = "";

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> s;

	for (int i = 1; i <= s.size() - 2; i++)
	{
		for (int j = 1; j <= s.size() - i - 1; j++)
		{
			string res = "";

			string a = s.substr(0, i);
			string b = s.substr(i, j);
			string c = s.substr(i + j);

			reverse(a.begin(), a.end());
			reverse(b.begin(), b.end());
			reverse(c.begin(), c.end());

			res = a + b + c;

			if (ans == "")
				ans = res;
			else if (ans > res)
				ans = res;
		}
	}

	cout << ans;

	return 0;
}