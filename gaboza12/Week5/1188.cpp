#include<bits/stdc++.h>

using namespace std;

int n, m;

int GCD(int a, int b)
{
	if (a % b == 0)
		return b;

	return GCD(b, a % b);
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	int ans = m - GCD(n, m);

	cout << ans << "\n";

	return 0;
}