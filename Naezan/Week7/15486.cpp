#include <bits/stdc++.h>

using namespace std;

int N;

vector<pair<int, int>> vec;

int maxm[1'500'001];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N;

	vec.resize(N + 1, pair<int,int>());
	for (int i = 1; i <= N; ++i)
	{
		int t, p;
		cin >> t >> p;

		vec[i].first = t;
		vec[i].second = p;
	}

	for (int i = 1; i <= N; ++i)
	{
		//상담이 끝나는 시간
		int endi = i + vec[i].first - 1;

		maxm[i] = max(maxm[i - 1], maxm[i]);

		//상담이 퇴사일을 넘어가면 X
		if (endi > N)
		{
			continue;
		}

		maxm[endi] = max(vec[i].second + maxm[i - 1], maxm[endi]);
	}

	cout << maxm[N];

	return 0;
}