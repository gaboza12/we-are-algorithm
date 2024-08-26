#include <bits/stdc++.h>

using namespace std;

int T;

//n개로 만들 수 있는 가장 작은 수
//점화식을 못찾음
// dp[n] = dp[n - idx] * 10 + num[idx];
long long dp[101];

//각 갯수별 제일 작은 숫자
int num[9] = { 0, 0, 1, 7, 4, 2, 0, 8 };

void calc(int _n)
{
	//가장 큰 수
	vector<int>  vec;
	if (_n % 2 == 0)
	{
		//몫만큼 1
		int s = (_n / 2);
		for (int i = 0; i < s; ++i)
		{
			vec.push_back(1);
		}
	}
	else
	{
		//몫 - 1만큼 1, 맨처음 7
		vec.push_back(7);
		for (int i = 0; i < (_n / 2) - 1; ++i)
		{
			vec.push_back(1);
		}
	}

	for (int i = 0; i < vec.size(); ++i)
	{
		cout << vec[i];
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	memset(dp, (long long)108, sizeof(dp));

	dp[2] = 1;
	dp[3] = 7;
	dp[4] = 4;
	dp[5] = 2;
	dp[6] = 6;
	dp[7] = 8;

	//가장 작은 수(약간의 감각이 필요한 연산?)
	for (int i = 8; i <= 100; ++i) //주어진 성냥개비 개수
	{
		for (int j = 2; j < 8; ++j) //사용한 성냥개비 개수
		{
			if (i - j <= 1)
			{
				continue;
			}

			dp[i] = min(dp[i], dp[i - j] * 10 + num[j]); //데칼코마니
		}
	}

	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		int n;
		cin >> n;
		cout << dp[n] << " ";
		calc(n);
		cout << endl;
	}

	return 0;
}