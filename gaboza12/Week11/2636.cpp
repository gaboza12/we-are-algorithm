#include <bits/stdc++.h>

using namespace std;

int n, m;

int ans = 0;
int cnt = 0;

bool flag = true;

int board[105][105];
int board2[105][105];

bool vis[105][105];

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

void board_copy()
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			vis[i][j] = false;
			board2[i][j] = board[i][j];
		}
	}
}

void flag_check()
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (board[i][j] == 1)
			{
				flag = true;
				return;
			}
		}
	}

	flag = false;
}

void bfs()
{
	board_copy();

	board[0][0] = -1;
	vis[0][0] = true;

	queue<pair<int, int>> q;
	q.push({ 0, 0 });

	while (!q.empty())
	{
		pair<int, int> cur = q.front();
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nx = cur.first + dx[i];
			int ny = cur.second + dy[i];

			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;

			if (board[nx][ny] == 1 || vis[nx][ny])
				continue;

			vis[nx][ny] = true;
			board[nx][ny] = -1;
			q.push({ nx, ny });
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (board[i][j] == 1)
			{
				bool flag2 = false;
				for (int k = 0; k < 4; k++)
				{
					if (flag2)
						continue;

					int nx = i + dx[k];
					int ny = j + dy[k];

					if (nx < 0 || nx >= n || ny < 0 || ny >= m)
						continue;

					if (board[nx][ny] == -1 && vis[nx][ny])
					{
						board[i][j] = -1;
						flag2 = true;
					}
				}
			}
		}
	}

	ans++;
}

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
		}
	}

	flag_check();
	
	while (flag)
	{
		bfs();

		flag_check();
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (board2[i][j] == 1)
				cnt++;
		}
	}

	cout << ans << "\n" << cnt;

	return 0;
}