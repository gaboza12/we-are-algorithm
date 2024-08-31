#include <bits/stdc++.h>

using namespace std;


int N, M;

int board[101][101];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> M;

	for (int i = 1; i <= N; ++i)
	{
		for (int j = 1; j <= N; ++j)
		{
			if (i != j && board[i][j] == 0)
			{
				board[i][j] = 200;
			}
		}
	}

	for (int i = 0; i < M; ++i)
	{
		int a, b;
		cin >> a >> b;

		board[a][b] = 1;
		board[b][a] = 1;
	}

	//10¸¸
	for (int i = 1; i <= N; ++i)
	{
		for (int j = 1; j <= N; ++j)
		{
			for (int k = 1; k <= N; ++k)
			{
				board[j][k] = min(board[j][k], board[j][i] + board[i][k]);
			}
		}
	}

	int ans = 20'000;
	int x, y;
	for (int i = 1; i <= N; ++i)
	{
		for (int j = i + 1; j <= N; ++j)
		{
			int temp = 0;
			for (int k = 1; k <= N; ++k)
			{
				temp += min(board[i][k], board[j][k]);
			}

			if (ans > temp)
			{
				ans = temp;
				x = i;
				y = j;
			}
		}
	}

	cout << x << ' ';
	cout << y << ' ';
	cout << ans * 2 << ' ';

	return 0;
}