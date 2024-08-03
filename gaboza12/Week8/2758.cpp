#include<bits/stdc++.h>

using namespace std;

int t, n, m;

long long dp[2005][15];

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> t;

	for (int i = 1; i < 2005; i++)
	{
		for (int j = 1; j < 15; j++)
		{
			if (j == 1)
			{
				dp[i][j] = 1;
				continue;
			}
			for (int k = 1; k < i / 2 + 1; k++)
			{
				dp[i][j] += dp[k][j - 1];
			}
		}
	}

	while (t--)
	{
		cin >> n >> m;
		long long ans = 0;

		for (int i = 1; i < m + 1; i++)
		{
			ans += dp[i][n];
		}
		cout << ans << "\n";
	}
	
	return 0;
}