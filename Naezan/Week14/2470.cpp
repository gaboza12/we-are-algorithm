#include <bits/stdc++.h>

using namespace std;

int N;

vector<int> vec;

int a, b;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N;

	vec.resize(N);
	for (int i = 0; i < N; ++i)
	{
		cin >> vec[i];
	}

	sort(vec.begin(), vec.end());

	//n을 하나 선정하고 이분탐색으로 최적의 값을 찾는  NlogN 방법
	//투포인터로 N번안에 해결하는 방법

	int st = 0;
	int en = N - 1;
	long long feature = vec[st] + vec[en];
	a = st; b = en;

	while (st < en)
	{
		long long temp = vec[st] + vec[en];
		if (temp < 0)
		{
			if (abs(feature) > abs(temp))
			{
				feature = temp;
				a = st;
				b = en;
			}
			++st;
		}
		else if(temp > 0)
		{
			if (abs(feature) > abs(temp))
			{
				feature = temp;
				a = st;
				b = en;
			}
			--en;
		}
		else
		{
			a = st;
			b = en;
			break;
		}
	}

	cout << vec[a] << ' ' << vec[b];

	return 0;
}