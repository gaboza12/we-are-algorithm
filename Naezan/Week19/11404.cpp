#include <bits/stdc++.h>

using namespace std;

int N, M;

vector<vector<long long>> vec;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> M;

	vec.resize(N, vector<long long>());
	for (int i = 0; i < N; ++i)
	{
		vec[i].resize(N, INT_MAX);
	}

	for (int i = 0; i < M; ++i)
	{
		long long s, e, p;
		cin >> s >> e >> p;
		vec[s - 1][e - 1] = min(vec[s - 1][e - 1], p);
	}

	for (int i = 0; i < N; ++i)
	{
		vec[i][i] = 0;
	}

	for (int m = 0; m < N; ++m)
	{
		for (int s = 0; s < N; ++s)
		{
			for (int e = 0; e < N; ++e)
			{
				vec[s][e] = min(vec[s][e], vec[s][m] + vec[m][e]);
			}
		}
	}

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			if (vec[i][j] == INT_MAX)
			{
				cout << 0 << ' ';
			}
			else
			{
				cout << vec[i][j] << ' ';
			}
		}

		cout << '\n';
	}

	return 0;
}