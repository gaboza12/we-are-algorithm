#include<bits/stdc++.h>

using namespace std;

int c, n;
int money[25], customer[25];
int dp[100005];

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> c >> n;

	for (int i = 1; i <= n; i++)
	{
		cin >> money[i] >> customer[i];
	}

	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= 100005; j++)
		{
			if (j - money[i] >= 0)
			{
				dp[j] = max(dp[j], dp[j - money[i]] + customer[i]);
			}
		}
	}

	for (int i = 1; i <= 100005; i++)
	{
		if (dp[i] >= c)
		{
			cout << i;
			break;
		}
	}
	
	return 0;
}