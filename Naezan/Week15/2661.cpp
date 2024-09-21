#include <bits/stdc++.h>

using namespace std;

int N;
string s;

bool issame(const string& ss, int idx)
{
	if (idx == 0)
	{
		return false;
	}

	for (int c = 1; c <= N; ++c)
	{
		int st = idx - (c * 2) + 1;
		int nst = st + c;

		if (st < 0)
		{
			break;
		}

		string temp1 = ss.substr(st, c);
		string temp2 = ss.substr(nst, c);

		if (temp1 == temp2)
		{
			return true;
		}
	}

	return false;
}

void calc(int n)
{
	if (n == N)
	{
		cout << s << '\n';
		exit(0);
	}

	for (int i = 1; i <= 3; ++i)
	{
		s[n] = (i + '0');
		if (!issame(s, n))
		{
			calc(n + 1);
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N;
	s.resize(N);

	calc(0);

	return 0;
}