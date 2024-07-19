#include<bits/stdc++.h>

using namespace std;

long long n, a, b, c, d;

long long ans = LLONG_MAX;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> a >> b >> c >> d;

	if (b * c > a * d)
	{
		swap(a, c);
		swap(b, d);
	}

	for (int i = 0; i < a; i++)
	{
		long long temp = (long long)ceil((double)(n - i * c) / a);

		bool flag = false;
		if (temp < 0)
		{
			flag = true;
			temp = 0;
		}

		ans = min(ans, temp * b + i * d);
		if (flag)
			break;
	}

	cout << ans;

	return 0;
}