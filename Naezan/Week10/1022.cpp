#include <bits/stdc++.h>

using namespace std;

int r1, c1, r2, c2;

int maxr, maxc;

int dirc = 2;
int curdir = 0;
int ax[4] = { 1, 0, -1, 0 };
int ay[4] = { 0, -1, 0, 1 };

unordered_map<int, int> board;

int calc(int x, int y)
{
	int maxi = max(abs(x), abs(y));
	int s = 2 * maxi + 1;
	int ss = s * s;

	if (y == maxi)
	{
		return ss + x - maxi;
	}
	else if (x == maxi)
	{
		return ss - (s * 4 - 5) - y + (x - 1);
	}
	else if (y == -maxi)
	{
		return (ss - maxi * 4) - x + y;
	}
	else
	{
		return (ss + x * 2) + y + x;
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> r1 >> c1 >> r2 >> c2;

	int big = 0;
	vector<int> vec;
	for (int i = r1; i <= r2; ++i)
	{
		for (int j = c1; j <= c2; ++j)
		{
			int temp = calc(j, i);
			big = max(big, temp);
			vec.push_back(temp);
		}
	}

	for (int i = 0; i <= r2 - r1; ++i)
	{
		for (int j = 0; j <= c2 - c1; ++j)
		{
			int temp = vec[i * (c2 - c1 + 1) + j];

			int whitec = to_string(big).length() - to_string(temp).length();

			for (int k = 0; k < whitec; ++k)
			{
				cout << ' ';
			}
			cout << temp << ' ';
		}
		cout << '\n';
	}

	return 0;
}