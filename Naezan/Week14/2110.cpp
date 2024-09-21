#include <bits/stdc++.h>

using namespace std;

int N, C;

vector<int> vec;

long long ans;

int getmaxwificount(int dist)
{
	int c = 1;
	int st = vec[0];

	for (int i = 1; i < N; ++i)
	{
		if (vec[i] - st >= dist)
		{
			++c;
			st = vec[i];
		}
	}

	return c;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> C;

	vec.resize(N);
	for (int i = 0; i < N; ++i)
	{
		cin >> vec[i];
	}

	sort(vec.begin(), vec.end());

	long long st = 1;
	long long en = 0x7fffffff - 1;

	while (st < en)
	{
		//max dist
		long long dist = (st + en) / 2;

		//dist까지 설치할 수 있는 공유기 수가 C보다 작으면 거리가 너무 크다는 뜻
		if (getmaxwificount(dist) < C)
		{
			en = dist;
		}
		else
		{
			st = dist + 1;
			ans = max(ans, dist);
		}
	}

	cout << ans;

	return 0;
}