#include <bits/stdc++.h>

using namespace std;

int n, m, k;

int board1[105][105];
int board2[105][105];
int ans[105][105];

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> board1[i][j];
		}
	}

	cin >> m >> k;

	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < k; j++)
		{
			cin >> board2[i][j];
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < k; j++)
		{
			for (int l = 0; l < m; l++)
			{
				ans[i][j] += board1[i][l] * board2[l][j];
			}
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < k; j++)
		{
			cout << ans[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}