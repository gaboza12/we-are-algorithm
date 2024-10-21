#include <bits/stdc++.h>

using namespace std;

int n, m;

bool item[105][105];

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	for (int i = 0; i < 105; i++)
	{
		for (int j = 0; j < 105; j++)
		{
			if (i == j)
				item[i][j] = true;
		}
	}

	for (int i = 0; i < m; i++)
	{
		int a, b;

		cin >> a >> b;

		item[a][b] = true;
	}

	for (int k = 1; k <= n; k++)
	{
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= n; j++)
			{
				item[i][j] = item[i][j] || (item[i][k] && item[k][j]);
			}
		}
	}

	for (int i = 1; i <= n; i++)
	{
		int cnt = 0;

		for (int j = 1; j <= n; j++)
		{
			if (item[i][j] == false && item[j][i] == false)
				cnt++;
		}

		cout << cnt << "\n";
	}

	return 0;
}