#include "bits/stdc++.h"

using namespace std;

int N, d, k, C;

vector<int> vec1;
vector<int> vec2;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> d >> k >> C;

	vec1.resize(N, 0);
	vec2.resize(d + 1, 0);

	for (int i = 0; i < N; ++i)
	{
		cin >> vec1[i];
	}

	//(0~k-1)
	int c = 0;
	for (int i = 0; i < k; ++i)
	{
		if (vec2[vec1[i]] == 0)
		{
			++c;
		}
		++vec2[vec1[i]];
	}

	int ans = 0;

	if (vec2[C] == 0)
	{
		ans = max(c + 1, ans);
	}
	else
	{
		ans = max(c, ans);
	}

	int st = 1;
	int en = k;
	while (st != N)
	{
		if (vec2[vec1[en]] == 0)
		{
			++c;
		}
		++vec2[vec1[en]];

		if (vec2[vec1[st - 1]] == 1)
		{
			--c;
		}
		--vec2[vec1[st - 1]];

		if (vec2[C] == 0)
		{
			ans = max(c + 1, ans);
		}
		else
		{
			ans = max(c, ans);
		}

		++st;
		++en;
		en %= N;
	}

	cout << ans;

	return 0;
}

