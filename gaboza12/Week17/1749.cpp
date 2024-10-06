#include <bits/stdc++.h>

using namespace std;

int board[205][205];
int psum[205][205];

int n, m;

int ans = -1e9 - 10;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> board[i][j];
			psum[i + 1][j + 1] = psum[i + 1][j] + psum[i][j + 1] - psum[i][j] + board[i][j];
		}
	}

	for (int x1 = 1; x1 <= n; x1++)
	{
		for (int y1 = 1; y1 <= m; y1++)
		{
			for (int x2 = x1; x2 <= n; x2++)
			{
				for (int y2 = y1; y2 <= m; y2++)
				{
					ans = max(ans, psum[x2][y2] - psum[x1 - 1][y2] - psum[x2][y1 - 1] + psum[x1 - 1][y1 - 1]);
				}
			}
		}
	}

	cout << ans;

	return 0;
}