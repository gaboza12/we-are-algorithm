#include <bits/stdc++.h>

using namespace std;

int N, M, R;
int ans;

vector<int> items;
vector<vector<int>> road;
vector<bool> check;

void calc(int curl, int s)
{
	check[s] = true;

	for (int i = 0; i < N; ++i)
	{
		if (road[s][i] == 0)
		{
			continue;
		}

		if (road[s][i] + curl <= M)
		{
			calc(road[s][i] + curl, i);
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> M >> R;

	road.resize(N, vector<int>());
	for (int i = 0; i < N; ++i)
	{
		road[i].resize(N);
	}

	items.resize(N);
	for (int i = 0; i < N; ++i)
	{
		cin >> items[i];
	}

	for (int i = 0; i < R; ++i)
	{
		int s, e, l;
		cin >> s >> e >> l;
		road[s - 1][e - 1] = l;
		road[e - 1][s - 1] = l;
	}

	//각 지역으로 떨어졌을 때 수색범위 내에 있는 모든 길의 갯수 탐색
	for (int i = 0; i < N; ++i)
	{
		check.clear();
		check.resize(N);
		calc(0, i);

		int temp = 0;
		for (int j = 0; j < N; ++j)
		{
			if (check[j])
			{
				temp += items[j];
			}
		}
		ans = max(ans, temp);
	}

	cout << ans;

	return 0;
}