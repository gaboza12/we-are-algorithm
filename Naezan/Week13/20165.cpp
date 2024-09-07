#include <bits/stdc++.h>

using namespace std;

int N, M, r;

std::vector<std::vector<int>> vec;
std::vector<std::vector<char>> board;

int ans;

enum Dir
{
	L, R, U, D, X
};

int ax[4] = { -1, 1, 0, 0 };
int ay[4] = { 0, 0, -1, 1 };

Dir Convert(char d)
{
	switch (d)
	{
	case 'E':
		return R;
	case 'W':
		return L;
	case 'S':
		return D;
	case 'N':
		return U;
	}

	return X;
}

void attack(int x, int y, char d)
{
	if (board[y][x] == 'F')
	{
		return;
	}

	++ans;
	board[y][x] = 'F';

	int movec = vec[y][x];
	Dir dir = Convert(d);

	for (int i = 1; i < movec; ++i)
	{
		x += ax[dir];
		y += ay[dir];

		if (x < 0 || y < 0 || x >= M || y >= N)
		{
			break;
		}

		if (board[y][x] == 'S')
		{
			++ans;
			board[y][x] = 'F';
			movec = max(movec, i + vec[y][x]);
		}
	}
}

void defence(int x, int y)
{
	board[y][x] = 'S';
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> M >> r;

	vec.resize(N);
	for (auto& v : vec)
	{
		v.resize(M);
	}

	board.resize(N);
	for (auto& v : board)
	{
		v.resize(M, 'S');
	}

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			cin >> vec[i][j];
		}
	}

	for (int i = 0; i < r; ++i)
	{
		int x, y;
		char d;

		cin >> y >> x >> d;

		attack(x - 1, y - 1, d);

		cin >> y >> x;

		defence(x - 1, y - 1);
	}

	cout << ans << '\n';
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			cout << board[i][j] << ' ';
		}
		cout << '\n';
	}

	return 0;
}