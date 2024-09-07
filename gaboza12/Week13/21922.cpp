#include <bits/stdc++.h>

using namespace std;

int board[2005][2005];
bool vis[2005][2005];

int n, m;

vector<pair<int, int>> aircon;

int ans = 0;

void Top(pair<int, int> p);
void Bottom(pair<int, int> p);
void Right(pair<int, int> p);
void Left(pair<int, int> p);

void func(pair<int, int> p)
{
	Top(p);
	Bottom(p);
	Right(p);
	Left(p);
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
			
			if (board[i][j] == 9)
			{
				aircon.push_back({ i, j });
				vis[i][j] = true;
			}
		}
	}

	for (int i = 0; i < aircon.size(); i++)
	{
		func(aircon[i]);
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (vis[i][j] == true)
				ans++;
		}
	}

	cout << ans;

	return 0;
}

void Top(pair<int, int> p)
{
	queue<pair<int, int>> q;
	q.push(p);

	while (!q.empty())
	{
		pair<int, int> cur = q.front();
		q.pop();

		vis[cur.first][cur.second] = true;

		int nx = cur.first - 1;
		int ny = cur.second;

		if (nx < 0 || nx >= n || ny < 0 || ny >= m)
			continue;

		if (board[nx][ny] == 2)
		{
			Bottom({ nx, ny });
		}
		else if (board[nx][ny] == 3)
		{
			Right({ nx, ny });
		}
		else if (board[nx][ny] == 4)
		{
			Left({ nx, ny });
		}
		else if (board[nx][ny] == 0 || board[nx][ny] == 1)
		{
			q.push({ nx, ny });
		}
	}
}

void Bottom(pair<int, int> p)
{
	queue<pair<int, int>> q;
	q.push(p);

	vis[p.first][p.second] = true;

	while (!q.empty())
	{
		pair<int, int> cur = q.front();
		q.pop();

		vis[cur.first][cur.second] = true;

		int nx = cur.first + 1;
		int ny = cur.second;

		if (nx < 0 || nx >= n || ny < 0 || ny >= m)
			continue;

		if (board[nx][ny] == 2)
		{
			Top({ nx, ny });
		}
		else if (board[nx][ny] == 3)
		{
			Left({ nx, ny });
		}
		else if (board[nx][ny] == 4)
		{
			Right({ nx, ny });
		}
		else if (board[nx][ny] == 0 || board[nx][ny] == 1)
		{
			q.push({ nx, ny });
		}
	}
}

void Right(pair<int, int> p)
{
	queue<pair<int, int>> q;
	q.push(p);

	vis[p.first][p.second] = true;

	while (!q.empty())
	{
		pair<int, int> cur = q.front();
		q.pop();

		vis[cur.first][cur.second] = true;

		int nx = cur.first;
		int ny = cur.second + 1;

		if (nx < 0 || nx >= n || ny < 0 || ny >= m)
			continue;

		if (board[nx][ny] == 1)
		{
			Left({ nx, ny });
		}
		else if (board[nx][ny] == 3)
		{
			Top({ nx, ny });
		}
		else if (board[nx][ny] == 4)
		{
			Bottom({ nx, ny });
		}
		else if (board[nx][ny] == 0 || board[nx][ny] == 2)
		{
			q.push({ nx, ny });
		}
	}
}

void Left(pair<int, int> p)
{
	queue<pair<int, int>> q;
	q.push(p);

	vis[p.first][p.second] = true;

	while (!q.empty())
	{
		pair<int, int> cur = q.front();
		q.pop();

		vis[cur.first][cur.second] = true;

		int nx = cur.first;
		int ny = cur.second - 1;

		if (nx < 0 || nx >= n || ny < 0 || ny >= m)
			continue;

		if (board[nx][ny] == 1)
		{
			Right({ nx, ny });
		}
		else if (board[nx][ny] == 3)
		{
			Bottom({ nx, ny });
		}
		else if (board[nx][ny] == 4)
		{
			Top({ nx, ny });
		}
		else if (board[nx][ny] == 0 || board[nx][ny] == 2)
		{
			q.push({ nx, ny });
		}
	}
}