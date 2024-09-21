#include <bits/stdc++.h>

using namespace std;

int n, k;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> k;

	int start = 1, end = k, mid = 0;
	int ans = 0;

	while (start <= end)
	{
		mid = (start + end) / 2;

		int cnt = 0;

		for (int i = 1; i <= n; i++)
		{
			cnt += min(n, mid / i);
		}

		if (cnt >= k)
		{
			ans = mid;
			end = mid - 1;
		}
		else
		{
			start = mid + 1;
		}
	}

	cout << ans;

	return 0;
}
