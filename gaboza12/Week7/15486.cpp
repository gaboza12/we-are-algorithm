#include<bits/stdc++.h>

using namespace std;

int n;

int t[1500005];
int p[1500005];
int dp[1500005];

int ans = 0;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n;

	for (int i = 1; i <= n; i++)
	{
		cin >> t[i] >> p[i];
	}

	for (int i = 1; i <= n + 1; i++)
	{
		ans = max(ans, dp[i]);
		if (i + t[i] > n + 1)
			continue;

		dp[i + t[i]] = max(dp[i + t[i]], ans + p[i]);
	}

	cout << ans;
	
	return 0;
}