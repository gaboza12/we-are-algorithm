#include <bits/stdc++.h>

using namespace std;

int N, M;

long long ans;

vector<long long> presum;
vector<long long> cache;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> M;
	presum.resize(N + 1);
	cache.resize(1001, 0);

	for (int i = 1; i <= N; ++i)
	{
		long long n;
		cin >> n;
		presum[i] = presum[i - 1] + n;

		//구간합의 나머지(s)
		long long s = presum[i] % M;
		//나머지를 캐싱
		++cache[s];
	}

	//구간들의 나머지가 같거나 나머지가 0이거나
	for (int i = 0; i < cache.size(); i++)
	{
		//nC2
		ans += cache[i] * (cache[i] - 1) / 2;
	}

	//0으로 딱 나누어 떨어지는 나머지
	ans += cache[0];

	cout << ans;

	return 0;
}