#include <bits/stdc++.h>

using namespace std;

int N;

char board[3100][6200];

void func(int x, int y, int n)
{
	if (n == 3)
	{
		board[x][y] = '*';
		board[x + 1][y - 1] = '*';
		board[x + 1][y + 1] = '*';

		for (int i = 0; i < 5; i++)
		{
			board[x + 2][y - 2 + i] = '*';
		}

		return;
	}

	func(x, y, n / 2);
	func(x + n / 2, y - n / 2, n / 2);
	func(x + n / 2, y + n / 2, n / 2);
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < 2 * N; j++)
		{
			board[i][j] = ' ';
		}
	}

	func(0, N - 1, N);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < 2 * N - 1; j++)
		{
			cout << board[i][j];
		}
		cout << "\n";
	}

	return 0;
}