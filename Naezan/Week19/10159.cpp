#include <bits/stdc++.h>

using namespace std;

int N, M;

vector<vector<int>> dir;
vector<vector<bool>> ans;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> M;

	dir.resize(N, vector<int>());
	for (int i = 0; i < N; ++i)
	{
		dir[i].resize(N, 0);
	}

	ans.resize(N, vector<bool>());
	for (int i = 0; i < N; ++i)
	{
		ans[i].resize(N, false);
	}

	for (int i = 0; i < N; ++i)
	{
		ans[i][i] = true;
	}

	for (int i = 0; i < M; ++i)
	{
		int a, b;
		cin >> a >> b;
		dir[a - 1][b - 1] = 1;
		dir[b - 1][a - 1] = -1;
		ans[a - 1][b - 1] = true;
		ans[b - 1][a - 1] = true;
	}

	for (int k = 0; k < N; ++k)
	{
		for (int s = 0; s < N; ++s)
		{
			for (int e = 0; e < N; ++e)
			{
				if (dir[s][k] == 0 || dir[k][e] == 0)
				{
					continue;
				}

				if (dir[s][k] == dir[k][e])
				{
					dir[s][e] = dir[s][k];
					dir[e][s] = dir[s][k] * -1;
					ans[s][e] = true;
					ans[e][s] = true;
				}
			}
		}
	}

	for (int i = 0; i < N; ++i)
	{
		int c = 0;
		for (int j = 0; j < N; ++j)
		{
			if (!ans[i][j])
			{
				++c;
			}
		}

		cout << c << '\n';
	}

	return 0;
}