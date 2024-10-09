#include <bits/stdc++.h>

using namespace std;

int N;
long long K, ans;

vector<long long> presum;
unordered_map<long long, int> cache;

//누적합의 값들의 갯수를 카운트해서 해시맵에 저장해두거나 맵에 저장해둠
//누적합들을 순회하면서 k - 맵이있은값이 해당 누적합에 부합하는 갯수를 ans에 더해주면됨

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> K;

	presum.resize(N + 1, 0);

	for (int i = 1; i <= N; ++i)
	{
		long long n;
		cin >> n;
		presum[i] = presum[i - 1] + n;
		//누적합 - 부분누적합 = K

		//그 값 자체가 K라면
		if (presum[i] == K)
		{
			++ans;
		}

		long long s = presum[i] - K;
		if (cache.count(s) > 0)
		{
			ans += cache[s];
		}

		++cache[presum[i]];
	}

	cout << ans;

	return 0;
}