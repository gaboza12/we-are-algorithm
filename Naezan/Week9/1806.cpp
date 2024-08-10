#include "bits/stdc++.h"

using namespace std;

int N, S;

long long ans = 100'001;

vector<int> arr;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> S;

	arr.resize(N, 0);
	for (int i = 0; i < N; ++i)
	{
		int n;
		cin >> n;
		arr[i] = n;
	}

	long long st = 0;
	long long en = 1;

	long long sum = arr[st];

	while (st < en)
	{
		if (sum < S)
		{
			if (en >= arr.size())
			{
				break;
			}

			sum += arr[en++];
		}
		else
		{
			ans = min(ans, en - st);

			sum -= arr[st++];
		}
	}

	if (ans == 100'001)
	{
		cout << 0;
	}
	else
	{
		cout << ans;
	}

	return 0;
}

