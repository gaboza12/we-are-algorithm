#include <bits/stdc++.h>

using namespace std;

int N, M;

long long ans = -600'000'001;

//누적합구하고 누적합내부에서 2중포문돌면서 내부에서 브루트포스수행
vector<vector<long long>> vec;
vector<vector<long long>> presum;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> M;

	vec.resize(N + 1);
	presum.resize(N + 1);
	for (int i = 0; i <= N; ++i)
	{
		vec[i].resize(M + 1);
		presum[i].resize(M + 1);
	}

	for (int i = 1; i <= N; ++i)
	{
		for (int j = 1; j <= M; ++j)
		{
			cin >> vec[i][j];
			presum[i][j] = presum[i - 1][j] + presum[i][j - 1] - presum[i - 1][j - 1] + vec[i][j];
			//부분합 중 최대 구하기

			ans = max(vec[i][j], ans);
			for (int y = 1; y <= i; ++y)
			{
				for (int x = 1; x <= j; ++x)
				{
					long long temppresum = presum[i][j] - presum[i][x - 1] - presum[y - 1][j] + presum[y - 1][x- 1];
					ans = max(temppresum, ans);
				}
			}
		}
	}

	cout << ans;

	return 0;
}