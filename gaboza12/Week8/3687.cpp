#include<bits/stdc++.h>

using namespace std;

int t, n;

int num[10] = { 0, 0, 1, 7, 4, 2, 0, 8, 10, 18};//성냥개비로 만들 수 있는 가장 작은 수

long long dp[105];

//숫자 : 성냥개비 수
//1 : 2 / 2 : 5 / 3 : 5 / 4 : 4 / 5 : 5 / 6 : 6 / 7 : 3 / 8 : 7 / 9 : 6 / 0 : 6


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> t;

	for (int i = 0; i < 10; i++)
	{
		dp[i] = num[i];
	}

	dp[6] = 6;//첫자리에 0 불가

	for (int i = 10; i <= 100; i++)
	{
		dp[i] = LLONG_MAX;
		for (int j = 2; j <= 7; j++)
		{
			dp[i] = min(dp[i], dp[i - j] * 10 + num[j]);
		}
	}

	while (t--)
	{
		cin >> n;

		cout << dp[n] << " ";

		while (n)
		{
			if (n % 2 == 1)
			{
				cout << "7";
				n -= 3;
			}
			else
			{
				cout << "1";
				n -= 2;
			}
		}

		cout << "\n";
	}

	return 0;
}