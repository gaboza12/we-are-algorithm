#include <bits/stdc++.h>

using namespace std;

int N, K;

int ans;
vector<int> arr;
vector<int> arr2;

//맨처음 재귀로 접근 -> 시간초과 -> 종이에 적어보니 제일 큰 간격만 없애면 된다는걸 깨달음

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> K;

	for (int i = 0; i < N; ++i)
	{
		int n;
		cin >> n;
		arr.push_back(n);
	}

	sort(arr.begin(), arr.end());

	for (int i = 1; i < N; ++i)
	{
		if (i - 1 < arr.size())
		{
			ans += abs(arr[i] - arr[i - 1]);
			arr2.push_back(abs(arr[i] - arr[i - 1]));
		}
		
	}

	//오름차순 정렬
	if (!arr2.empty())
	{
		sort(arr2.begin(), arr2.end(), greater<int>());
	}

	// K - 1번반복하면서 가장 큰 간격의 값 제거
	for (int i = 0; i < K - 1; ++i)
	{
		if (i < arr2.size())
		{
			ans -= arr2[i];
		}
	}

	cout << ans;

	return 0;
}