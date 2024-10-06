#include <bits/stdc++.h>

using namespace std;

long long psum[100005];

int n, m;

long long sum, ans;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		int temp;
		cin >> temp;

		sum += temp;
		psum[sum % m]++;
	}
		
	for (int i = 0; i <= m; i++)
	{
		ans += ((psum[i] * (psum[i] - 1)) / 2);
	}

	cout << ans + psum[0];

	return 0;
}