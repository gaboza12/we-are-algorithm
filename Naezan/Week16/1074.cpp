#include <bits/stdc++.h>

using namespace std;

int N, R, C;

int ax[3] = { 1, 0, 1 };
int ay[3] = { 0, 1, 1 };

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> R >> C;

	int s = pow(2, N);

	int w = s / 2;
	int h = s / 2;

	int pr = 0;
	int pc = 0;

	int ans = 0;
	if (N != 1)
	{
		while (true)
		{
			if (R >= pr + h)
			{
				ans += h * w * 2;
				pr += h;
			}

			if (C >= pc + w)
			{
				ans += w * h;
				pc += w;
			}

			if (w == 2 && h == 2)
			{
				break;
			}

			w /= 2;
			h /= 2;
		}
	}

	int temppr = pr;
	int temppc = pc;
	for (int i = 0; i < 3; ++i)
	{
		if (temppr == R && temppc == C)
		{
			break;
		}

		temppr = pr + ay[i];
		temppc = pc + ax[i];
		++ans;
	}

	cout << ans << '\n';

	return 0;
}