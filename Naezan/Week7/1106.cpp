#include <bits/stdc++.h>

using namespace std;

int C, N;

vector<pair<int, int>> vec;

int minc[110'1];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> C >> N;

	for (int i = 0; i < N; ++i)
	{
		int p, c;
		cin >> p >> c;
		vec.emplace_back(c, p);
	}

	//클라이언트가 작은 순으로 정렬
	sort(vec.begin(), vec.end());

	for (int i = 0; i < N; ++i)
	{
		for (int j = vec[i].first; j <= C + 100; ++j)
		{
			if (j % vec[i].first != 0 && minc[j - vec[i].first] == 0)
			{
				continue;
			}

			if (minc[j] != 0)
			{
				minc[j] = min(minc[j], minc[j - vec[i].first] + vec[i].second);
			}
			else
			{
				minc[j] = minc[j - vec[i].first] + vec[i].second;
			}
		}
	}

	int ans = INT_MAX;
	for (int i = C; i <= C + 100; ++i)
	{
		if (minc[i] != 0)
		{
			ans = min(minc[i], ans);
		}
	}

	cout << ans;

	return 0;
}