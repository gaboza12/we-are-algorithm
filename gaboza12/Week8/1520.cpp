#include<bits/stdc++.h>

using namespace std;

int m, n;

int board[505][505];
bool vis[505][505];
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

int dp[505][505];

int ans = 0;

int dfs(int a, int b)
{
	if (a == m - 1 && b == n - 1)
		return 1;

	if (dp[a][b] != -1)
		return dp[a][b];

	dp[a][b] = 0;

	for (int i = 0; i < 4; i++)
	{
		int nx = a + dx[i];
		int ny = b + dy[i];

		if (nx < 0 || nx >= m || ny < 0 || ny >= n)
			continue;

		if (vis[nx][ny] || board[nx][ny] >= board[a][b])
			continue;

		dp[a][b] += dfs(nx, ny);
	}

	return dp[a][b];
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> m >> n;

	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> board[i][j];
			dp[i][j] = -1;
		}
	}

	vis[0][0] = true;
	ans = dfs(0, 0);

	cout << ans;
	
	return 0;
}