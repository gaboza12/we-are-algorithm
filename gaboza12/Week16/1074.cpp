#include <bits/stdc++.h>

using namespace std;

int n, r, c;

int ans = 0;

void func(int x, int y, int sz)
{
	if (x == r && y == c)
	{
		cout << ans;
		return;
	}

	if (x <= r && y <= c && x + sz > r && y + sz > c)
	{
		func(x, y, sz / 2);
		func(x, y + sz / 2, sz / 2);
		func(x + sz / 2, y, sz / 2);
		func(x + sz / 2, y + sz / 2, sz / 2);
	}
	else
	{
		ans += sz * sz;
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	cin >> n >> r >> c;

	func(0, 0, pow(2, n));

	return 0;
}