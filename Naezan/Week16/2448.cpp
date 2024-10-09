#include <bits/stdc++.h>

using namespace std;

int N;

vector<vector<char>> vec;

void calc(int tx, int ty, int n)
{
	if (n == 3)
	{
		//출력
		vec[ty][tx] = '*';
		vec[ty + 1][tx - 1] = '*';
		vec[ty + 1][tx + 1] = '*';
		vec[ty + 2][tx - 2] = '*';
		vec[ty + 2][tx - 1] = '*';
		vec[ty + 2][tx] = '*';
		vec[ty + 2][tx + 1] = '*';
		vec[ty + 2][tx + 2] = '*';
		return;
	}

	calc(tx - n / 2, ty + n / 2, n / 2); //좌
	calc(tx, ty, n / 2); //가운데
	calc(tx + n / 2, ty + n / 2, n / 2); //우
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N;
	vec.resize(N, vector<char>());
	for (int i = 0;i < N;++i)
	{
		vec[i].resize(N * 2 - 1, ' ');
	}

	calc(N - 1, 0, N);

	for (int i = 0;i < N;++i)
	{
		for (int j = 0;j < 2 * N - 1;++j)
		{
			cout << vec[i][j];
		}
		cout << '\n';
	}

	return 0;
}