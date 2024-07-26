#include<bits/stdc++.h>

using namespace std;

int n, k;

int coin[105];
int dp[10005];

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> k;

	for (int i = 1; i <= n; i++)
	{
		cin >> coin[i];
	}

	for (int i = 1; i <= k; i++)
	{
		dp[i] = 10005;
	}

	for (int i = 1; i <= n; i++)
	{
		for (int j = coin[i]; j <= k; j++)
		{
			dp[j] = min(dp[j], dp[j - coin[i]] + 1);
		}
	}

	if (dp[k] == 10005)
		cout << -1;
	else
		cout << dp[k];
	
	return 0;
}