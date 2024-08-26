#include <bits/stdc++.h>

using namespace std;

//재귀로는 불가능 -> 반복문으로했을 때 20억번으로 계산되어 불가능
// -> dp로 풀어야 했고 2차원 배열을 사용해야한다는 것까지 파악 -> 점화식을 생각못함
// -> 일부 답지 참고

int T;

long long dp[11][2001];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	//0번 사용하는 경우엔 마지막 번호가 어떻든 1가지
	for (int j = 0; j <= 2000; ++j)
	{
		dp[0][j] = 1;
	}

	//i는 사용한 횟수
	//j는 사용한 마지막 번호
	//dp[i][j] = dp[i][j - 1] + dp[i - 1][j / 2];
	for (int i = 1; i <= 10; ++i)
	{
		for (int j = 1; j <= 2000; ++j)
		{
			dp[i][j] = dp[i][j - 1] + dp[i - 1][j / 2];
		}
	}

	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		int n, m;
		cin >> n >> m;

		cout << dp[n][m] << endl;
	}

	return 0;
}