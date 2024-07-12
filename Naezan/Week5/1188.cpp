#include <bits/stdc++.h>

using namespace std;

int N, M;
int ans;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> M;

	int extr = N % M;
	if (extr == 0)
	{
		ans = 0;
	}
	else
	{
		for (int i = 1; i <= M; ++i)
		{
			if (N * i % M != 0)
			{
				++ans;
			}
		}
	}

	cout << ans;

	return 0;
}