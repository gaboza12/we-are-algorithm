#include <bits/stdc++.h>

using namespace std;

int board[105][105];
int vis[105][105];//false : 안넘어짐, true : 넘어짐

int n, m, r;

int ans = 0;

void attack(int x, int y, char d)
{
	if (vis[x][y])//넘어져 있으면 아무일X
		return;

	vis[x][y] = true;

	int height = board[x][y] - 1;//도미노 높이

	int res = 1;

	int idx = 0;

	while (height)
	{
		height--;
		idx++;
		
		int nx = 0, ny = 0;
		switch (d)
		{
		case 'E':
			nx = x;
			ny = y + idx;

			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;

			if (vis[nx][ny])
				continue;

			if (board[nx][ny] > height)//넘어지는게 더 높으면 높이변경
				height = board[nx][ny] - 1;

			vis[nx][ny] = true;
			res++;
			
			break;

		case 'W':
			nx = x;
			ny = y - idx;

			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;

			if (vis[nx][ny])
				continue;

			if (board[nx][ny] > height)
				height = board[nx][ny] - 1;

			vis[nx][ny] = true;
			res++;

			break;

		case 'N':
			nx = x - idx;
			ny = y;

			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;

			if (vis[nx][ny])
				continue;

			if (board[nx][ny] > height)
				height = board[nx][ny] - 1;

			vis[nx][ny] = true;
			res++;

			break;

		case 'S':
			nx = x + idx;
			ny = y;

			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;

			if (vis[nx][ny])
				continue;

			if (board[nx][ny] > height)
				height = board[nx][ny] - 1;

			vis[nx][ny] = true;
			res++;

			break;
		}
	}

	ans += res;
}

void defense(int x, int y)
{
	if (!vis[x][y])//안넘어져 있으면 아무일X
		return;

	vis[x][y] = false;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m >> r;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> board[i][j];
		}
	}

	for (int i = 0; i < r; i++)
	{
		int x, y;
		char d;

		cin >> x >> y >> d;
		attack(x - 1, y - 1, d);
		
		cin >> x >> y;
		defense(x - 1, y - 1);
	}

	cout << ans << "\n";

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (vis[i][j])
				cout << "F ";
			else
				cout << "S ";
		}
		cout << "\n";
	}
	
	return 0;
}