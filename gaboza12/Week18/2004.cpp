#include <bits/stdc++.h>

using namespace std;

//조합 nCr = n! / (r! * (n - r)!)
//끝자리 0 : 10 = 2 x 5, 100 = 2 x 2 x 5 x 5

int n, m;

int func(int a, int b)
{
	int cnt = 0;

	for (long long i = b; i <= a; i *= b)
	{
		cnt += a / i;
	}

	return cnt;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	int two = 0, five = 0;

	two = func(n, 2) - func(n - m, 2) - func(m, 2);
	five = func(n, 5) - func(n - m, 5) - func(m, 5);

	cout << min(two, five) << "\n";

	return 0;
}