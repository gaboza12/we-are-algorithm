#include <bits/stdc++.h>

using namespace std;

long long psum[200005];

int n, k;

map<long long, long long> m;

long long ans = 0;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> k;

	for (int i = 1; i <= n; i++)
	{
		cin >> psum[i];
		psum[i] += psum[i - 1];

		if (psum[i] == k)
			ans++;
	}

	for (int i = 1; i <= n; i++)
	{
		ans += m[psum[i] - k];
		m[psum[i]]++;
	}

	cout << ans;

	return 0;
}