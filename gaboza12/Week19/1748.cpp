#include <bits/stdc++.h>

using namespace std;

int n;

long long ans = 0;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n;

	for (int i = 100000000; i >= 1; i /= 10)
	{
		if (n / i >= 1)
		{
			ans += n - i + 1;
		}
	}

	cout << ans;

	return 0;
}