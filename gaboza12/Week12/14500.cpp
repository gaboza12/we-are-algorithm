#include <bits/stdc++.h>

using namespace std;

int n, m;

int board[505][505];

int ans = 0;

void func(int a, int b)
{
	int res = 0;

	//ㅡ
	if (b + 3 < m)
	{
		for (int i = 0; i < 4; i++)
		{
			res += board[a][b + i];
		}

		ans = max(ans, res);
	}

	res = 0;

	//ㅣ
	if (a + 3 < n)
	{
		for (int i = 0; i < 4; i++)
		{
			res += board[a + i][b];
		}

		ans = max(ans, res);
	}

	res = 0;

	//ㅁ
	if (a + 1 < n && b + 1 < m)
	{
		res += board[a][b] + board[a + 1][b] + board[a][b + 1] + board[a + 1][b + 1];

		ans = max(ans, res);
	}

	res = 0;

	if (a + 2 < n && b + 1 < m)
	{
		res+=board[a][b] + board[a + 1][b] + board[a + 2][b] + board[a + 2][b + 1];

		ans = max(ans, res);
	}

	res = 0;

	if (a + 2 < n && b - 1 >= 0)
	{
		res += board[a][b] + board[a + 1][b] + board[a + 2][b] + board[a + 2][b - 1];

		ans = max(ans, res);
	}

	res = 0;

	if (a - 1 >= 0 && b + 2 < m)
	{
		res += board[a][b] + board[a][b + 1] + board[a][b + 2] + board[a - 1][b + 2];

		ans = max(ans, res);
	}

	res = 0;

	if (a + 1 <n && b + 2 < m)
	{
		res += board[a][b] + board[a][b + 1] + board[a][b + 2] + board[a + 1][b + 2];

		ans = max(ans, res);
	}

	res = 0;

	if (a - 2 >= 0 && b - 1 >= 0)
	{
		res += board[a][b] + board[a - 1][b] + board[a - 2][b] + board[a - 2][b - 1];

		ans = max(ans, res);
	}

	res = 0;

	if (a - 2 >= 0 && b + 1 < m)
	{
		res += board[a][b] + board[a - 1][b] + board[a - 2][b] + board[a - 2][b + 1];

		ans = max(ans, res);
	}

	res = 0;

	if (a + 1 < n && b - 2 >= 0)
	{
		res += board[a][b] + board[a][b - 1] + board[a][b - 2] + board[a + 1][b - 2];

		ans = max(ans, res);
	}

	res = 0;

	if (a - 1 >=0 && b - 2 >= 0)
	{
		res += board[a][b] + board[a][b - 1] + board[a][b - 2] + board[a - 1][b - 2];

		ans = max(ans, res);
	}

	res = 0;

	if (a + 2 < n && b + 1 < m)
	{
		res += board[a][b] + board[a + 1][b] + board[a + 1][b + 1] + board[a + 2][b + 1];

		ans = max(ans, res);
	}

	res = 0;

	if (a + 2 < n && b - 1 >= 0)
	{
		res += board[a][b] + board[a + 1][b] + board[a + 1][b - 1] + board[a + 2][b - 1];

		ans = max(ans, res);
	}

	res = 0;

	if (a - 1 >= 0 && b + 2 < m)
	{
		res += board[a][b] + board[a][b + 1] + board[a - 1][b + 1] + board[a - 1][b + 2];

		ans = max(ans, res);
	}

	res = 0;

	if (a + 1 < n && b + 2 < m)
	{
		res += board[a][b] + board[a][b + 1] + board[a + 1][b + 1] + board[a + 1][b + 2];

		ans = max(ans, res);
	}

	res = 0;

	if (a + 1 < n && b + 1 < m && b - 1 >= 0)
	{
		res += board[a][b] + board[a + 1][b] + board[a + 1][b + 1] + board[a + 1][b - 1];

		ans = max(ans, res);
	}

	res = 0;

	if (a - 1 >= 0 && b + 1 < m && b - 1 >= 0)
	{
		res += board[a][b] + board[a - 1][b] + board[a - 1][b + 1] + board[a - 1][b - 1];

		ans = max(ans, res);
	}

	res = 0;

	if (a - 1 >= 0 && a + 1 < n && b + 1 < m)
	{
		res += board[a][b] + board[a][b + 1] + board[a - 1][b + 1] + board[a + 1][b + 1];

		ans = max(ans, res);
	}

	res = 0;

	if (a - 1 >= 0 && a + 1 < n && b - 1 >=0)
	{
		res += board[a][b] + board[a][b - 1] + board[a - 1][b - 1] + board[a + 1][b - 1];

		ans = max(ans, res);
	}
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

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			func(i, j);
		}
	}

	cout << ans;

	return 0;
}