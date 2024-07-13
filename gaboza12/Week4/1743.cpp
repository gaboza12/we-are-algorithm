#include<bits/stdc++.h>
using namespace std;

int n, m, k;

int board[105][105];
bool vis[105][105];

int ans = 0;

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

void bfs(int x, int y)
{
	queue<pair<int, int>> q;
	q.push({ x, y });

	vis[x][y] = true;

	int cnt = 0;

	while (!q.empty())
	{
		pair<int, int> cur = q.front();
		q.pop();
		
		cnt++;

		for (int i = 0; i < 4; i++)
		{
			int nx = dx[i] + cur.first;
			int ny = dy[i] + cur.second;

			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;

			if (board[nx][ny] == 0 || vis[nx][ny])
				continue;

			q.push({ nx, ny });
			vis[nx][ny] = true;
			
		}
	}

	ans = max(ans, cnt);
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m >> k;

	for (int i = 0; i < k; i++)
	{
		int r, c;

		cin >> r >> c;

		board[r - 1][c - 1] = 1;
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (board[i][j] == 1 && !vis[i][j])
			{
				bfs(i, j);
			}
		}
	}

	cout << ans;

	return 0;
}