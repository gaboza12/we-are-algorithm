#include <bits/stdc++.h>

using namespace std;

int N, K;

vector<int> vec;

int mink[10'001];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> K;

	vec.resize(N, 0);
	for (int i = 0; i < N; ++i)
	{
		int n;
		cin >> n;
		vec[i] = n;
	}

	sort(vec.begin(), vec.end());

	for (int i = 0; i < N; ++i)
	{
		for (int j = vec[i]; j <= K; ++j)
		{
			//이전에 동전을 사용하지 않았다면 못함
			if (mink[j - vec[i]] == 0 && 
			j % vec[i] != 0)
			{
				continue;
			}
			//배수면 정상적으로 비교 가능
			//배수가 아니면 이전에 동전을 사용했어야 함

			if (mink[j] != 0)
			{
				mink[j] = min(mink[j], mink[j - vec[i]] + 1);
			}
			else
			{
				mink[j] = mink[j - vec[i]] + 1;
			}
		}
	}

	if (mink[K] == 0)
	{
		cout <<  -1;
	}
	else
	{
		cout << mink[K];
	}

	return 0;
}