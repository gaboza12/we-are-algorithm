#include <bits/stdc++.h>

using namespace std;

int N, K;

int ans;

vector<int> arr;

// 센서 문제가 풀리면 이 문제도 손쉽게 풀림

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> K;

	int prev;
	for (int i = 0; i < N; ++i)
	{
		int cur;
		cin >> cur;

		if (i >= 1)
		{
			ans += cur - prev;
			arr.push_back(cur - prev);
		}

		prev = cur;
	}

	sort(arr.begin(), arr.end(), greater<int>());

	for (int i = 0; i < K - 1; ++i)
	{
		ans -= arr[i];
	}

	cout << ans;

	return 0;
}