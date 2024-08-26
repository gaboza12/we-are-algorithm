#include <bits/stdc++.h>

using namespace std;

int odd_board[305][305];
int even_board[305][305];

int dx[8] = { -2,-2,-1,1,2,2,-1,1 };
int dy[8] = { -1,1,2,2,1,-1,-2,-2 };

int n, m, k, t;//방크기, 곰팡이개수, 검사좌표개수, 청소검사남은일수

queue<pair<int, int>> q;//곰팡이좌표

void odd()
{
	int sz = q.size();
	while (sz--)
	{
		pair<int, int> cur = q.front();
		q.pop();

		for (int i = 0; i < 8; i++)
		{
			int nx = cur.first + dx[i];
			int ny = cur.second + dy[i];

			if (nx < 1 || ny < 1 || nx > n || ny > n)
				continue;

			if (odd_board[nx][ny] == 1)
				continue;

			q.push({ nx, ny });
			odd_board[nx][ny] = 1;
		}
	}
}
void even()
{
	int sz = q.size();
	while (sz--)
	{
		pair<int, int> cur = q.front();
		q.pop();

		for (int i = 0; i < 8; i++)
		{
			int nx = cur.first + dx[i];
			int ny = cur.second + dy[i];

			if (nx < 1 || ny < 1 || nx > n || ny > n)
				continue;

			if (even_board[nx][ny] == 1)
				continue;

			q.push({ nx, ny });
			even_board[nx][ny] = 1;
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m >> k >> t;

	for (int i = 0; i < m; i++)
	{
		int x, y;
		cin >> x >> y;

		q.push({ x, y });
	}

	for (int i = 1; i <= t; i++)
	{
		if (i % 2 == 1)
			odd();
		else
			even();
	}

	bool ans = true;

	while(k--)
	{
		int x, y;

		cin >> x >> y;

		if (t % 2 == 1)
		{
			if (odd_board[x][y] == 1)
				ans = false;
		}
		else
		{
			if (even_board[x][y] == 1)
				ans = false;
		}
	}

	if (ans)
		cout << "NO";
	else
		cout << "YES";

	return 0;
}