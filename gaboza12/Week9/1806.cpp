#include<bits/stdc++.h>

using namespace std;

int n, s;

int arr[100005];

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> s;

	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}

	int start = 0, end = 0, sum = 0, ans = 1e9 + 10;

	while (start <= end)
	{
		if (sum >= s)
		{
			ans = min(ans, end - start);
			sum -= arr[start];
			start++;
			continue;
		}

		if (end == n)
			break;

		sum += arr[end];
		end++;
	}

	if (ans == 1e9 + 10)
		cout << 0;
	else
		cout << ans;

	return 0;
}